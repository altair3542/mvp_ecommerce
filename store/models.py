from django.db import models
from decimal import Decimal

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
