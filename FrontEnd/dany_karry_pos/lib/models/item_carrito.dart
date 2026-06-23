// lib/models/item_carrito.dart

// Importamos el molde de producto porque lo vamos a usar acá adentro
import 'producto.dart';

class ItemCarrito {
  final Producto producto; // El objeto producto completo (con su id, nombre, precio)
  int cantidad;            // Una variable que sí puede cambiar (sumar o restar cantidad)

  // Constructor: Al crear un ítem en el carrito, por defecto la cantidad es 1
  ItemCarrito({
    required this.producto,
    this.cantidad = 1,
  });

  // Una propiedad calculada (Getter): Calcula el subtotal de esta línea al vuelo
  // Multiplica el precio de ese producto por la cantidad seleccionada
  int get subtotal => producto.precio * cantidad;
}