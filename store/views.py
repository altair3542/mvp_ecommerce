# from django.shortcuts import render, get_object_or_404
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.

# def product_list(request):
#     """
#     vista basada en una funcion que se trae todos los productos activos
#     """
#     products = Product.objects.active()
#     context = {
#         "products": products,
#     }
#     return render(request, "store/product_list.html", context)

# def product_detail(request, slug):
#     """
#     Vista basada en funcion que muestra el detalle de un producto
#     """
#     product = get_object_or_404(Product.objects.active(), slug=slug)
#     context = {
#         "product": product
#     }
#     return render(request, "store/product_detail.html", context)


class ProductListView(ListView):
    """
    vista basada en clase para listar productos activos
    """
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        """
        usamos el manager personalizado para devolver solo los productos activos
        """
        return Product.objects.all()

class ProductDetailView(DetailView):
    """
    vista basada en clase para el detalle de un producto
    """

    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Product.objects.active()
