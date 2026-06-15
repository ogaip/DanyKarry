# ventas/models.py
from django.db import models
from django.conf import settings

# Create your models here.


class Producto(models.Model):
    CATEGORIAS_CHOICES = [
        ('COMIDA', 'Comida'),
        ('BEBIDAS', 'Bebidas'),
        ('COMBOS', 'Combos'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        # Eliminamos self.imagen de aquí para evitar caídas catastróficas por nulos
        return f"{self.nombre} - Gs. {self.precio:.0f}"


class Venta(models.Model):
    METODOS_PAGO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('QR', 'QR'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]

    cajero = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(
        max_length=15, choices=METODOS_PAGO_CHOICES, default='EFECTIVO')
    total = models.DecimalField(max_digits=12, decimal_places=0, default=0)

    def __str__(self):
        return f"Venta #{self.id} - Total: Gs. {self.total:.0f} ({self.fecha_hora.strftime('%d/%m/%Y %H:%M')})"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)

    precio_unitario = models.DecimalField(max_digits=10, decimal_places=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} (Venta #{self.venta.id})"