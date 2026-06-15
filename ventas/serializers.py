# ventas/serializer.py
from django.db import models
from rest_framework import serializers
from .models import Producto, Venta, DetalleVenta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetalleVentaInputSerializer(serializers.Serializer):
    """ serializer auxiliar para validad los productos que vienen del carrito"""
    producto_id = serializers.IntegerField()
    cantidad = serializers.IntegerField(min_value=1)

class VentaSerializer(serializers.ModelSerializer):
    productos = DetalleVentaInputSerializer(many=True, write_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'fecha_hora', 'metodo_pago', 'total', 'productos']
        read_only_fields = [ 'id', 'fecha_hora', 'total' ]

    def create(self, validated_data):
        productos_carrito = validated_data.pop('productos')

        request = self.context.get('request')
        cajero = request.user

        venta = Venta.objects.create(cajero=cajero, **validated_data)

        total_venta = 0

        for item in productos_carrito:
            try: 
                producto = Producto.objects.get(id=item['producto_id'], activo=True)
            except Producto.DoesNotExist:
                raise serializers.ValidationError(f"El producto con ID {item['producto_id']} no existe o no está activo.")
            
            precio_historico = producto.precio
            subtotal_item = precio_historico * item['cantidad']
            total_venta += subtotal_item

            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=item['cantidad'],
                precio_unitario=precio_historico,
                subtotal=subtotal_item
            )

        # Actualizamos el total definitivo de la venta de forma automática
        venta.total = total_venta
        venta.save()

        return venta