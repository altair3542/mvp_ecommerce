# 🎓 Mini E-Commerce: Django y Programación Orientada a Objetos

[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic-yellow.svg)]()

## 📚 Descripción del Proyecto

Este es un proyecto académico diseñado para enseñar **Programación Orientada a Objetos Intermedia con Django** a través de la construcción de un mini e-commerce funcional (catálogo de productos, carrito, checkout básico y usuarios).

El proyecto utiliza un **enfoque progresivo de 7 sesiones** donde se exploran conceptos de POO dentro de Django: modelos ricos, CBV (Class-Based Views), mixins, servicios y patrones de diseño.

### 🎓 Nivel Previo Esperado

Los estudiantes deben tener conocimientos de:

- **Python básico**: funciones, listas, diccionarios, módulos
- **POO básica**: clases, objetos, `__init__`, atributos y métodos
- **Django básico**: proyecto/app, modelos simples, migraciones, admin, vistas y templates

## 📋 Plan de Estudios (7 Sesiones)

### **Sesión 1** – Diseño del dominio y repaso de POO en contexto Django
🎯 **Objetivo**: Aterrizar el dominio del e-commerce y conectar POO con la arquitectura de Django.

**Contenido:**
- Repaso rápido de POO: clases, objetos, atributos, métodos
- Métodos de instancia, clase y estáticos
- Encapsulamiento básico y `@property`
- Arquitectura Django: patrón MTV vs MVC
- Dónde vive la POO: modelos, CBV, formularios, servicios
- Diseño del dominio: Product, Category, Customer, Order, OrderItem

**Práctica:**
- Crear proyecto y app `store`
- Implementar modelos `Category` y `Product`
- Registrar en admin y cargar datos de prueba

---

### **Sesión 2** – Modelos ricos en comportamiento y relaciones entre objetos
🎯 **Objetivo**: Profundizar en el modelado orientado a objetos usando los modelos de Django.

**Contenido:**
- Relaciones entre clases: composición y agregación
- `ForeignKey`, `OneToOneField`, `ManyToManyField`
- Modelos ricos: métodos de instancia (`price_with_tax`, `is_in_stock`)
- Métodos de clase y managers personalizados
- Buenas prácticas: lógica de negocio en modelos o servicios
- Evitar "fat views"

**Práctica:**
- Crear modelos `Customer`, `Order` y `OrderItem`
- Implementar métodos para totales y estados
- Crear `ProductManager` con `active()` y `by_category()`

---

### **Sesión 3** – Vistas basadas en clases (CBV) como herramienta de POO
🎯 **Objetivo**: Aprovechar herencia y composición mediante CBV.

**Contenido:**
- Funciones vs clases en vistas
- CBV genéricas: `ListView`, `DetailView`, `CreateView`, `UpdateView`
- Ciclo de vida y métodos a sobreescribir
- Herencia y reutilización: `BaseStoreView` para contexto común
- Mixins: `LoginRequiredMixin` y mixins propios

**Práctica:**
- Implementar `ProductListView` y `ProductDetailView`
- Crear `CategoryListMixin` reutilizable
- Navegar entre catálogo ↔ detalle

---

### **Sesión 4** – Carrito de compras: diseño orientado a objetos
🎯 **Objetivo**: Diseñar el carrito como componente OOP independiente del framework.

**Contenido:**
- Diseño de clases: `Cart` y `CartItem` como clases de dominio
- Composición: `Cart` contiene `CartItem`
- Gestión del carrito: sesión vs base de datos
- Desacoplar lógica del framework
- Buenas prácticas OOP: responsabilidad única

**Práctica:**
- Implementar `Cart` y `CartItem` en `cart.py`
- Crear vistas para agregar, listar y eliminar ítems
- Conectar con `Product` y la sesión

---

### **Sesión 5** – Checkout, formularios y validación orientada a objetos
🎯 **Objetivo**: Modelar el checkout con formularios, CBV y lógica OOP.

**Contenido:**
- Formularios en Django: `forms.Form` vs `ModelForm`
- Validación con `clean()` y `clean_<field>()`
- Flujo de checkout: `CheckoutForm` (envío, contacto)
- Servicios de dominio para confirmar orden
- Módulo `services.py` con coordinadores de modelos

**Práctica:**
- Crear `CheckoutForm`
- Implementar vista de checkout (`FormView`/`CreateView` custom)
- Crear servicio `create_order_from_cart(cart, customer)`

---

### **Sesión 6** – Usuarios, roles y mixins personalizados
🎯 **Objetivo**: Integrar autenticación, perfiles y patrones OOP para roles y permisos.

**Contenido:**
- Sistema de usuarios: `User` y `AbstractUser` (visión general)
- Perfil `Customer` con `OneToOne`
- Mixins de vistas: `LoginRequiredMixin`, `UserPassesTestMixin`
- Mixins propios: `CustomerRequiredMixin`, `StaffRequiredMixin`
- Patrones OOP: Template Method en CBV
- Mixins como forma de composición

**Práctica:**
- Asociar `Customer` con `User`
- Proteger checkout para usuarios autenticados
- Crear `CustomerOrdersView` con mixins

---

### **Sesión 7** – Refactor, pruebas y patrones para escalar
🎯 **Objetivo**: Consolidar lo aprendido, mejorar diseño OOP y dejar el proyecto listo para crecer.

**Contenido:**
- Revisión crítica del diseño: responsabilidades mezcladas
- Extracción de servicios/helpers/mixins
- Patrones aplicables: Strategy para métodos de pago o envío
- Factory simple para creación de órdenes
- Pruebas automatizadas: unittest/pytest con Django
- Pruebas para clases de dominio y servicios

**Práctica:**
- Implementar Strategy para costo de envío
- Tests para `Cart`, servicios y flujo de orden
- Documentar el diseño OOP en README

## 🎯 Objetivos de Aprendizaje

Al completar este curso, los estudiantes serán capaces de:

1. **Aplicar POO intermedia** en proyectos Django reales
2. **Diseñar modelos ricos** con lógica de negocio encapsulada
3. **Utilizar CBV y mixins** para reutilizar código eficientemente
4. **Implementar patrones de diseño** (Strategy, Factory, Service Layer)
5. **Gestionar relaciones complejas** entre entidades
6. **Escribir tests** para clases de dominio y servicios
7. **Desacoplar lógica de negocio** del framework
8. **Entender y aplicar** principios SOLID en Django

## 📊 Estado Actual del Proyecto

| Sesión | Tema | Estado | Implementado |
|--------|------|--------|--------------|
| **1** | Diseño del dominio y repaso POO | ✅ Completo | `Category`, `Product`, Admin |
| **2** | Modelos ricos y relaciones | 🚧 Pendiente | Falta: `Customer`, `Order`, `OrderItem` |
| **3** | Vistas basadas en clases (CBV) | ⏳ Por iniciar | - |
| **4** | Carrito de compras OOP | ⏳ Por iniciar | - |
| **5** | Checkout y formularios | ⏳ Por iniciar | - |
| **6** | Usuarios, roles y mixins | ⏳ Por iniciar | - |
| **7** | Refactor, pruebas y patrones | ⏳ Por iniciar | - |

### 🎯 Próximos Pasos

El proyecto actualmente está en la **Sesión 1**, con los modelos base `Category` y `Product` completamente documentados e implementados. Los siguientes pasos serán:

1. **Sesión 2**: Agregar modelos `Customer`, `Order` y `OrderItem` con relaciones
2. **Sesión 3**: Implementar vistas basadas en clases para el catálogo
3. **Sesión 4**: Desarrollar el sistema de carrito
4. **Sesión 5**: Crear el proceso de checkout
5. **Sesión 6**: Integrar sistema de usuarios y permisos
6. **Sesión 7**: Refactorizar y agregar tests

## 🏗️ Arquitectura del Proyecto

### Estructura de Directorios

```
mini_ecommerce/
│
├── manage.py                 # Script principal de Django
├── db.sqlite3               # Base de datos SQLite
├── README.md                # Este archivo
│
├── mini_ecommerce/          # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py          # Configuración global
│   ├── urls.py             # Rutas principales
│   ├── wsgi.py             # Configuración WSGI
│   └── asgi.py             # Configuración ASGI
│
└── store/                   # Aplicación principal (tienda)
    ├── __init__.py
    ├── models.py           # Modelos de datos (Category, Product)
    ├── admin.py            # Configuración del panel admin
    ├── views.py            # Lógica de vistas
    ├── apps.py             # Configuración de la app
    ├── tests.py            # Pruebas unitarias
    └── migrations/         # Migraciones de base de datos
```

## 🔑 Conceptos Clave de POO Implementados

### 1. **Clases y Objetos**

Los modelos de Django son clases que heredan de `models.Model`:

```python
class Category(models.Model):
    """Clase que representa una categoría de productos"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
```

**Concepto POO**: Cada instancia de `Category` es un objeto con sus propios atributos.

### 2. **Herencia**

Django utiliza herencia para extender funcionalidad:

```python
# Category hereda de models.Model
class Category(models.Model):
    # Hereda todos los métodos y atributos de Model
    pass
```

**Concepto POO**: Herencia permite reutilizar código y extender funcionalidad base.

### 3. **Encapsulamiento**

Los datos se protegen y se accede mediante métodos:

```python
@property
def product_count(self) -> int:
    """Propiedad computada que encapsula la lógica de conteo"""
    return self.products.count()
```

**Concepto POO**: El decorador `@property` encapsula la lógica interna y expone un atributo de solo lectura.

### 4. **Métodos de Instancia**

Operan sobre datos de una instancia específica:

```python
def price_with_tax(self, tax_rate: Decimal = Decimal("0.19")) -> Decimal:
    """Calcula el precio con impuestos para este producto"""
    return self.price * (Decimal("1") + tax_rate)
```

**Concepto POO**: `self` representa la instancia actual del objeto.

### 5. **Métodos de Clase**

Operan sobre la clase en lugar de instancias:

```python
@classmethod
def active(cls):
    """Retorna todos los productos activos"""
    return cls.objects.filter(is_active=True)
```

**Concepto POO**: `cls` representa la clase misma, no una instancia.

### 6. **Métodos Mágicos (Dunder Methods)**

Python permite personalizar el comportamiento de objetos:

```python
def __str__(self) -> str:
    """Define cómo se representa el objeto como string"""
    return str(self.name)
```

**Concepto POO**: `__str__` se invoca automáticamente con `str(objeto)` o `print(objeto)`.

### 7. **Relaciones entre Objetos**

Django implementa relaciones mediante Foreign Keys:

```python
category = models.ForeignKey(
    Category,
    related_name="products",
    on_delete=models.PROTECT
)
```

**Concepto POO**: Representa una relación "muchos a uno" entre Product y Category.

## 📊 Modelo de Datos

### Diagrama Completo del Sistema (Objetivo Final)

Este diagrama muestra el modelo de datos completo que se construirá a lo largo de las 7 sesiones:

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   Category   │         │   Product    │         │     User     │
├──────────────┤         ├──────────────┤         ├──────────────┤
│ PK id        │◄───┐    │ PK id        │         │ PK id        │
│    name      │    │    │    name      │         │    username  │
│    slug      │    │    │    slug      │         │    email     │
└──────────────┘    │    │ FK category  │         │    password  │
                    └────│    price     │         └──────┬───────┘
                         │    stock     │                │
                         │    is_active │                │ 1:1
                         └──────────────┘                │
                                                         │
┌──────────────┐         ┌──────────────┐         ┌────▼─────────┐
│     Cart     │         │   CartItem   │         │   Customer   │
├──────────────┤         ├──────────────┤         ├──────────────┤
│    items[]   │◄────────│ FK product   │         │ PK id        │
│    total     │    *    │    quantity  │         │ FK user      │
│ + add()      │         │    subtotal  │         │    phone     │
│ + remove()   │         └──────────────┘         │    address   │
└──────────────┘                                  └──────┬───────┘
                                                         │
                                                         │ 1:N
                         ┌──────────────┐         ┌─────▼────────┐
                         │  OrderItem   │         │    Order     │
                         ├──────────────┤         ├──────────────┤
                         │ PK id        │    ┌────│ PK id        │
                         │ FK order     │◄───┘    │ FK customer  │
                         │ FK product   │    *    │    total     │
                         │    quantity  │         │    status    │
                         │    price     │         │    created_at│
                         │    subtotal  │         └──────────────┘
                         └──────────────┘
```

**Leyenda:**
- `PK` = Primary Key (Clave primaria)
- `FK` = Foreign Key (Clave foránea)
- `1:N` = Relación uno a muchos
- `1:1` = Relación uno a uno
- `*` = Composición (el contenedor posee los elementos)

### Diagrama Actual (Sesión 1)

```
┌─────────────────┐         ┌─────────────────┐
│    Category     │         │     Product     │
├─────────────────┤         ├─────────────────┤
│ PK id           │◄────┐   │ PK id           │
│    name         │     │   │    name         │
│    slug         │     │   │    slug         │
└─────────────────┘     │   │ FK category_id  │
                        └───│    description  │
                            │    price        │
                            │    is_active    │
                            │    created_at   │
                            │    updated_at   │
                            └─────────────────┘
```

**Relación**: Una categoría puede tener muchos productos (1:N)

### Category Model

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | AutoField | Identificador único (PK) |
| `name` | CharField | Nombre de la categoría |
| `slug` | SlugField | URL-friendly identifier |

**Métodos destacados:**
- `__str__()`: Representación en string
- `product_count`: Propiedad que retorna cantidad de productos

### Product Model

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | AutoField | Identificador único (PK) |
| `name` | CharField | Nombre del producto |
| `slug` | SlugField | URL-friendly identifier |
| `category` | ForeignKey | Relación con Category |
| `description` | TextField | Descripción detallada |
| `price` | DecimalField | Precio (10 dígitos, 2 decimales) |
| `is_active` | BooleanField | Estado activo/inactivo |
| `created_at` | DateTimeField | Fecha de creación |
| `updated_at` | DateTimeField | Fecha de actualización |

**Métodos destacados:**
- `__str__()`: Representación en string
- `price_with_tax(tax_rate)`: Calcula precio con impuestos
- `active()`: Método de clase que retorna productos activos

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/altair3542/mini_ecommerce.git
cd mini_ecommerce
```

2. **Crear entorno virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django
```

4. **Ejecutar migraciones**
```bash
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder al proyecto**
- Aplicación: http://127.0.0.1:8000/
- Panel Admin: http://127.0.0.1:8000/admin/

## 🛠️ Uso del Panel de Administración

### Acceso al Admin

1. Inicia sesión en `/admin/` con las credenciales del superusuario
2. Verás las secciones **Categories** y **Products**

### Crear una Categoría

1. Click en **"Categories"** → **"Add Category"**
2. Ingresa el nombre (ej: "Laptops")
3. El slug se generará automáticamente
4. Click en **"Save"**

### Crear un Producto

1. Click en **"Products"** → **"Add Product"**
2. Completa los campos:
   - **Name**: Nombre del producto
   - **Slug**: Se genera automáticamente
   - **Category**: Selecciona una categoría
   - **Description**: Descripción detallada
   - **Price**: Precio (usa formato decimal: 999.99)
   - **Is active**: Marca para activar el producto
3. Click en **"Save"**

## 💡 Ejemplos de Uso

### Usando el Shell de Django

```bash
python manage.py shell
```

#### Crear una Categoría

```python
from store.models import Category
from decimal import Decimal

# Crear categoría
laptops = Category(name="Laptops", slug="laptops")
laptops.save()

# O usando create()
monitores = Category.objects.create(name="Monitores", slug="monitores")
```

#### Crear un Producto

```python
from store.models import Product, Category

categoria = Category.objects.get(slug="laptops")

producto = Product.objects.create(
    name="Laptop Dell XPS 13",
    slug="laptop-dell-xps-13",
    category=categoria,
    description="Laptop ultradelgada con procesador Intel i7",
    price=Decimal("1299.99"),
    is_active=True
)
```

#### Consultar Productos

```python
# Todos los productos
productos = Product.objects.all()

# Productos activos (usando método de clase)
activos = Product.active()

# Productos de una categoría específica
laptops = Product.objects.filter(category__slug="laptops")

# Calcular precio con impuestos
producto = Product.objects.first()
precio_con_iva = producto.price_with_tax()  # 19% por defecto
precio_con_21 = producto.price_with_tax(Decimal("0.21"))  # 21%
```

#### Relaciones Inversas

```python
# Obtener todos los productos de una categoría
categoria = Category.objects.get(slug="laptops")
productos = categoria.products.all()

# Contar productos de una categoría
cantidad = categoria.product_count  # Usa la propiedad
```

## 📖 Conceptos Avanzados

### 1. QuerySets y Lazy Evaluation

Los QuerySets de Django son "perezosos" - no ejecutan la consulta hasta que se evalúan:

```python
# No ejecuta consulta SQL
productos = Product.objects.filter(is_active=True)

# Ahora sí ejecuta la consulta
for producto in productos:
    print(producto.name)
```

### 2. Decimal vs Float para Dinero

**Siempre usa `Decimal` para dinero**, no `float`:

```python
from decimal import Decimal

# ✅ CORRECTO
precio = Decimal("19.99")

# ❌ INCORRECTO (problemas de precisión)
precio = 19.99
```

### 3. related_name en ForeignKey

Permite acceder a la relación inversa:

```python
# En Product:
category = models.ForeignKey(Category, related_name="products")

# Ahora desde Category:
categoria = Category.objects.first()
productos = categoria.products.all()  # ← related_name
```

### 4. on_delete en ForeignKey

Controla qué sucede cuando se elimina el objeto relacionado:

- `CASCADE`: Elimina productos cuando se elimina la categoría
- `PROTECT`: Impide eliminar categoría si tiene productos
- `SET_NULL`: Establece en NULL (requiere null=True)
- `SET_DEFAULT`: Establece valor por defecto

```python
category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT  # No permite eliminar categorías con productos
)
```

### 5. Índices de Base de Datos

Mejoran la velocidad de búsqueda:

```python
class Meta:
    indexes = [
        models.Index(fields=["slug"]),      # Índice simple
        models.Index(fields=["is_active"]),  # Índice en booleano
    ]
```

## 🧪 Testing

### Ejecutar Tests

```bash
python manage.py test store
```

### Ejemplo de Test

```python
from django.test import TestCase
from decimal import Decimal
from store.models import Category, Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.categoria = Category.objects.create(
            name="Test Category",
            slug="test-category"
        )

    def test_price_with_tax(self):
        producto = Product.objects.create(
            name="Test Product",
            slug="test-product",
            category=self.categoria,
            price=Decimal("100.00")
        )

        precio_con_iva = producto.price_with_tax(Decimal("0.19"))
        self.assertEqual(precio_con_iva, Decimal("119.00"))
```

## 🎨 Patrones de Diseño Implementados

A lo largo del curso se implementarán diversos patrones de diseño orientados a objetos:

### 1. **Model-View-Template (MVT)**
El patrón arquitectónico base de Django que separa:
- **Model**: Lógica de datos y negocio
- **View**: Lógica de presentación y control
- **Template**: Interfaz de usuario

### 2. **Active Record**
Los modelos de Django implementan este patrón:
```python
# El modelo conoce cómo persistirse
producto = Product(name="Laptop", price=999.99)
producto.save()  # Se guarda a sí mismo
```

### 3. **Manager Pattern**
Django usa managers para encapsular consultas:
```python
# Manager personalizado
class ProductManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)
```

### 4. **Template Method** (Sesión 3)
CBV implementan este patrón definiendo el flujo general:
```python
class ProductListView(ListView):
    # Sobreescribimos métodos específicos
    def get_queryset(self):
        return Product.active()
```

### 5. **Mixin Pattern** (Sesión 6)
Composición de comportamiento mediante herencia múltiple:
```python
class CustomerOrdersView(LoginRequiredMixin, CustomerRequiredMixin, ListView):
    # Combina comportamientos de múltiples mixins
    pass
```

### 6. **Strategy Pattern** (Sesión 7)
Para seleccionar algoritmos en tiempo de ejecución:
```python
# Diferentes estrategias de envío
class StandardShipping:
    def calculate(self, order): return 5.00

class ExpressShipping:
    def calculate(self, order): return 15.00
```

### 7. **Factory Pattern** (Sesión 7)
Para encapsular la creación de objetos complejos:
```python
class OrderFactory:
    @staticmethod
    def create_from_cart(cart, customer):
        # Lógica compleja de creación
        order = Order.objects.create(customer=customer)
        # ... crear OrderItems, calcular totales, etc.
        return order
```

### 8. **Service Layer Pattern** (Sesión 5)
Capa de servicios para coordinar operaciones:
```python
# services.py
class OrderService:
    def create_order_from_cart(self, cart, customer):
        # Coordina múltiples modelos
        pass
```

## 📝 Buenas Prácticas Aplicadas

1. **Docstrings Completos**: Toda clase y método está documentado con ejemplos
2. **Type Hints**: Uso de anotaciones de tipo Python para mayor claridad
3. **Nombres Descriptivos**: Variables y métodos con nombres claros y significativos
4. **Separación de Responsabilidades**: Cada modelo tiene una única responsabilidad (SRP)
5. **DRY (Don't Repeat Yourself)**: Reutilización de código mediante herencia y mixins
6. **Validación de Datos**: Uso de `unique=True`, `blank=False`, validators
7. **Uso de Decimal**: Para operaciones monetarias precisas (evitar float)
8. **Encapsulamiento**: Lógica de negocio dentro de los modelos
9. **Composición sobre Herencia**: Uso de mixins para compartir comportamiento
10. **Testing**: Pruebas automatizadas para lógica crítica

## 🔍 Características del Admin

### CategoryAdmin

- **list_display**: Muestra nombre, slug y cantidad de productos
- **search_fields**: Búsqueda por nombre y slug
- **prepopulated_fields**: Slug se genera automáticamente del nombre

### ProductAdmin

- **list_display**: Muestra información clave del producto
- **list_filter**: Filtros por categoría, estado y fecha
- **search_fields**: Búsqueda en nombre, slug y descripción
- **prepopulated_fields**: Slug automático

## 🎓 Guía de Uso para Estudiantes

### 📖 Cómo Seguir el Curso

Este repositorio está diseñado para seguirse **sesión por sesión**. Cada sesión incluye:

1. **Conceptos teóricos** explicados en este README
2. **Código de ejemplo** en los archivos del proyecto
3. **Prácticas guiadas** descritas en cada sesión
4. **Ejercicios propuestos** al final del README

### 🔄 Flujo de Trabajo Recomendado

Para cada sesión:

1. **Lee la teoría** de la sesión correspondiente en este README
2. **Examina el código** de los archivos relacionados
3. **Ejecuta el proyecto** y prueba las funcionalidades
4. **Completa las prácticas** propuestas para esa sesión
5. **Experimenta** modificando el código
6. **Comparte** tus dudas y soluciones con el instructor

### 💡 Consejos para Aprender

- **No copies y pegues**: Escribe el código manualmente para interiorizarlo
- **Usa el shell de Django**: Experimenta con los modelos en tiempo real
- **Lee los docstrings**: Toda función y clase está documentada
- **Haz preguntas**: Los errores son oportunidades de aprendizaje
- **Revisa los commits**: El historial muestra la evolución del proyecto

### � Debugging y Solución de Problemas

Si encuentras errores:

1. **Lee el traceback completo** - Django da mensajes de error descriptivos
2. **Usa el shell de Django** - Prueba tu código línea por línea
3. **Revisa la documentación** - Los docstrings tienen ejemplos
4. **Consulta el admin** - Verifica que los datos estén correctos
5. **Pregunta al instructor** - No te quedes atascado

## �📚 Recursos Adicionales

### Documentación Oficial

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- [Django Class-Based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)
- [Python POO](https://docs.python.org/3/tutorial/classes.html)

### Tutoriales Recomendados

- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Django for Beginners](https://djangoforbeginners.com/)
- [Real Python - Django](https://realpython.com/tutorials/django/)
- [Test-Driven Development with Django](https://testdriven.io/blog/django-first-principles/)

### Libros Sugeridos

- "Two Scoops of Django" - Daniel y Audrey Roy Greenfeld
- "Django for Professionals" - William S. Vincent
- "Object-Oriented Python" - Irv Kalb

## 🤝 Contribuciones

Este es un proyecto académico. Las contribuciones son bienvenidas a través de:

1. Fork del repositorio
2. Crear una rama con tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto es de uso académico y educativo.

## ✉️ Contacto

**Instructor**: Santiago Mesa Serna
**Email**: [sanmesaserna@gmail.com]
**GitHub**: [@altair3542](https://github.com/altair3542)

---

**Nota para Estudiantes**: Este proyecto está diseñado para aprender haciendo. No dudes en experimentar, romper cosas, y aprender de los errores. ¡La práctica hace al maestro! 🚀

## 🎓 Ejercicios Propuestos

### Nivel Básico
1. Crea 3 categorías y 5 productos usando el admin
2. Usa el shell para consultar productos de una categoría específica
3. Calcula el precio con impuestos de todos los productos

### Nivel Intermedio
4. Agrega un campo `stock` al modelo Product
5. Crea un método que indique si hay stock disponible
6. Implementa un método de clase que retorne productos con stock bajo

### Nivel Avanzado
7. Crea un modelo `Order` (Pedido) relacionado con Product
8. Implementa un sistema de descuentos
9. Añade validación personalizada a los modelos

---

**¡Feliz aprendizaje! 📚💻**
