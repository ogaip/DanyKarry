// lib/models/producto.dart

class Producto {
  // 1. Atributos: Definimos las propiedades con sus tipos estrictos
  final int id;
  final String nombre;
  final String categoria;
  final int precio; // Usamos int porque en Paraguay no usamos decimales para el Guaraní
  final bool activo;
  final String? imagen; // El signo '?' significa que puede ser Null (por si no tiene foto)

  // 2. Constructor: El molde básico para crear un producto en Dart
  Producto({
    required this.id,
    required this.nombre,
    required this.categoria,
    required this.precio,
    required this.activo,
    this.imagen, // No lleva 'required' porque es opcional (puede ser null)
  });

  // 3. Constructor Especial (Factory): Traduce el JSON de Django a un objeto Dart
  // Recibe un Map (Clave: String, Valor: Dinámico) que es exactamente como luce un JSON
  factory Producto.fromJson(Map<String, dynamic> json) {
    return Producto(
      id: json['id'],
      nombre: json['nombre'],
      categoria: json['categoria'],
      // Django envía el precio como un String con decimales (ej: "28000.00").
      // Lo convertimos a String, lo cortamos en el punto, y lo pasamos a un entero limpio.
      precio: int.parse(json['precio'].toString().split('.')[0]),
      activo: json['activo'] ?? true, // Si no viene el campo, por defecto es true
      imagen: json['imagen'],
    );
  }
}