// lib/providers/pos_provider.dart

import 'package:flutter/material.dart';
import 'dart:convert'; // Nos permite usar json.decode() para parsear lo que envíe Django
import 'package:http/http.dart'
    as http; // Para hacer peticiones GET y POST a la API
import '../models/producto.dart';
import '../models/item_carrito.dart';

class PosProvider extends ChangeNotifier {
  // 1. ESTADO (Las variables globales de nuestra app en memoria)
  List<Producto> _productos =
      []; // Lista privada con los 28 productos del backend
  List<Producto> get productos =>
      _productos; // Getter público para leer la lista

  final List<ItemCarrito> _carrito =
      []; // Lista privada de los ítems en el ticket
  List<ItemCarrito> get carrito => _carrito;

  String _categoriaSeleccionada = 'COMIDA'; // Filtro por defecto (.active)
  String get categoriaSeleccionada => _categoriaSeleccionada;

  bool _cargando =
      false; // Para mostrar un spinner de carga mientras descarga de Django
  bool get cargando => _cargando;

  // 2. FILTRADO (Como un filtro dinámico de JS)
  // Devuelve solo los productos que coinciden con la categoría activa de la botonera
  List<Producto> get productosFiltrados {
    return _productos
        .where((p) => p.categoria == _categoriaSeleccionada)
        .toList();
  }

  // 3. LOGICA DE NEGOCIO (Las funciones que alteran los datos)

  // Cambia la categoría activa (Comida, Bebidas, Combos)
  void cambiarCategoria(String nuevaCategoria) {
    _categoriaSeleccionada = nuevaCategoria;
    notifyListeners(); // 📢 ¡Silbato! Redibuja los productos en pantalla
  }

  // Agrega un producto al ticket de la caja
  void agregarProducto(Producto producto) {
    // Buscamos si el producto ya existe en el carrito
    final index = _carrito.indexWhere(
      (item) => item.producto.id == producto.id,
    );

    if (index >= 0) {
      // Si ya está, sumamos 1 a la cantidad de esa línea
      _carrito[index].cantidad++;
    } else {
      // Si no está, creamos un ítem nuevo (que por defecto inicia en cantidad = 1)
      _carrito.add(ItemCarrito(producto: producto));
    }
    notifyListeners(); // 📢 ¡Silbato! Actualiza el ticket visualmente y recalcula el total
  }

  // Resta cantidades o elimina del ticket si llega a cero
  void restarProducto(Producto producto) {
    final index = _carrito.indexWhere(
      (item) => item.producto.id == producto.id,
    );

    if (index >= 0) {
      if (_carrito[index].cantidad > 1) {
        _carrito[index].cantidad--;
      } else {
        _carrito.removeAt(index); // Si tiene 1 y le resta, se saca del ticket
      }
      notifyListeners(); // 📢 ¡Silbato!
    }
  }

  // Propiedad calculada (Getter): Suma todos los subtotales del carrito
  int get totalGeneral {
    return _carrito.fold(0, (suma, item) => suma + item.subtotal);
  }

  // 4. CONEXIÓN CON EL BACKEND (HTTP GET)
  Future<void> cargarProductos() async {
    _cargando = true;
    notifyListeners(); // Muestra el spinner de carga en la pantalla

    // URL de tu endpoint local en Django
    final url = Uri.parse('http://127.0.0.1:8000/api/ventas/productos/');

    try {
      final response = await http.get(url);

      if (response.statusCode == 200) {
        // json.decode transforma el String puro de la respuesta en una Lista dinámica
        final List<dynamic> data = json.decode(response.body);

        // Mapeamos cada JSON de la lista usando nuestro molde "factory" de Producto
        _productos = data.map((json) => Producto.fromJson(json)).toList();
      }
    } catch (e) {
      print("Error de conexión con Django: $e");
    } finally {
      _cargando = false;
      notifyListeners(); // Saca el spinner y dibuja los productos reales descárgados
    }
  }
}
