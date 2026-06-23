# ventas/urls.py
from django.urls import path
from .views import ListarProductosAPIView, RegistrarVentaAPIView

urlpatterns = [
    path('productos/', ListarProductosAPIView.as_view(), name='api-productos'),
    path('crear/', RegistrarVentaAPIView.as_view(), name='api-registrar-venta'),
]