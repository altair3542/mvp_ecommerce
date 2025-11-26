from django.db import models
from decimal import Decimal
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    """Representa una categoria del catalogo, por ejemplo, portatiles, monitores, teclados"""
    name = models.CharField("nombre", max_length=100, unique=True)
    slug = models.SlugField("slug", max_length=120, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self) -> str:
        return str(self.name)

    @property
    def product_count(self) -> int:
        """propiedad que devuelve cuantos productos tiene una categoria especifica, usando una relacion inversa 'products' definida en el modelo de Product"""
        return self.products.count()

class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def by_category(self, category_slug: str):
        return self.active().filter(category_slug=category_slug)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def by_category(self, category_slug: str):
        return self.get_queryset().by_category(category_slug)


class Product(models.Model):
    """representa un producto vendible en el mini e commerce."""
    name = models.CharField("nombre", max_length=200)
    slug = models.SlugField("slug", max_length=220, unique=True)
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.PROTECT,
        verbose_name="categoria",
    )
    description = models.TextField("descripcion", blank=True)
    price = models.DecimalField("precio", max_digits=10, decimal_places=2)
    is_active = models.BooleanField("activo", default=True)
    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self) -> str:
        return str(self.name)

    def price_with_tax(self, tax_rate: Decimal = Decimal("0.19")) -> Decimal:
        """Metodo de instancia que calcula el precio con impuesto, se usa la libreria decimal para evitar problemas de precision con dinero"""
        return self.price * (Decimal("1") + tax_rate)

    @classmethod
    def active(cls):
        """voy a devolver un query set con los productos activos, con una consulta, por ejemplo, Product.active()"""
        return cls.objects.filter(is_active=True)


# ==========================
# Customer
# ==========================

class Customer(models.Model):
    """
    Representa a un cliente del e-commerce.
    En esta sesión lo mantenemos independiente de django.contrib.auth.
    Más adelante lo podremos vincular a User mediante OneToOneField.
    """

    first_name = models.CharField("nombres", max_length=100)
    last_name = models.CharField("apellidos", max_length=150)
    email = models.EmailField("email", unique=True)
    phone = models.CharField("teléfono", max_length=20, blank=True)
    created_at = models.DateTimeField("creado", auto_now_add=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def total_orders(self) -> int:
        """
        Cantidad de órdenes que ha realizado este cliente.
        """
        return self.orders.count()

    def last_order(self):
        """
        Devuelve la última orden (o None si no tiene).
        """
        return self.orders.order_by("-created_at").first()


# ==========================
# Order y OrderItem
# ==========================

class Order(models.Model):
    """
    Representa una orden de compra realizada por un Customer.
    """

    STATUS_PENDING = "pending"
    STATUS_PAID = "paid"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pendiente"),
        (STATUS_PAID, "Pagada"),
        (STATUS_CANCELLED, "Cancelada"),
    ]

    customer = models.ForeignKey(
        Customer,
        related_name="orders",
        on_delete=models.CASCADE,  # composición: si se borra el cliente, se borran sus órdenes
        verbose_name="cliente",
    )
    status = models.CharField(
        "estado",
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "orden"
        verbose_name_plural = "órdenes"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Orden #{self.id} - {self.customer.full_name}"

    @property
    def is_paid(self) -> bool:
        return self.status == self.STATUS_PAID

    def total_items(self) -> int:
        """
        Total de unidades (sumando cantidades de todos los ítems).
        """
        return sum(item.quantity for item in self.items.all())

    def total_amount(self) -> Decimal:
        """
        Total monetario de la orden (suma de subtotales).
        """
        return sum(item.subtotal for item in self.items.all())

    def mark_paid(self):
        """
        Marca la orden como pagada y actualiza la fecha de actualización.
        """
        self.status = self.STATUS_PAID
        self.updated_at = timezone.now()
        self.save(update_fields=["status", "updated_at"])

    def mark_cancelled(self):
        """
        Marca la orden como cancelada.
        """
        self.status = self.STATUS_CANCELLED
        self.updated_at = timezone.now()
        self.save(update_fields=["status", "updated_at"])


class OrderItem(models.Model):
    """
    Representa una línea dentro de una orden (producto + cantidad + precio unitario).
    """

    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="orden",
    )
    product = models.ForeignKey(
        Product,
        related_name="order_items",
        on_delete=models.PROTECT,
        verbose_name="producto",
    )
    quantity = models.PositiveIntegerField("cantidad", default= 1)
    unit_price = models.DecimalField(
        "precio unitario",
        max_digits=10,
        decimal_places=2,
        help_text="Precio del producto en el momento de la compra.",
    )

    class Meta:
        verbose_name = "ítem de orden"
        verbose_name_plural = "ítems de orden"

    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name}"

    @property
    def subtotal(self) -> Decimal:
        """
        Subtotal = cantidad * precio unitario.
        """
        return self.unit_price * self.quantity
