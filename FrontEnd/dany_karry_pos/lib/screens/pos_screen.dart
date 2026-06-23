import 'package:flutter/material.dart';

class PosScreen extends StatelessWidget {
  const PosScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100], // Fondo gris claro (.bg-light de Bootstrap)
      appBar: AppBar(
        title: const Text('Danny Karry - Punto de Venta', style: TextStyle(color: Colors.white)),
        backgroundColor: Colors.red[800],
      ),
      body: Row(
        children: [
          // seccion 1 ( Izquierda): catalogo de productos. ocupa el 70% del ancho (flex: 7)
          Expanded(
            flex: 7,
            child: Container(
              color: Colors.white,
              child: Text(
                'Zona de productos (Grilla proximamente)', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)
                ),
              ),
            ),
            Container(width: 1, color: Colors.grey[300]),

          // SECCIÓN 2 (Derecha): El Ticket de la Caja. Ocupa el 30% del ancho (flex: 3)

          Expanded(
            flex: 3,
            child: Container(
              color: Colors.grey[50],
              child: const Center(
                child: Text(
                  'Ticket de Compra / Carrito',
                  style: TextStyle(fontSize: 18, color: Colors.grey),
                ),
              ),
            ),
          ),
          
        ],
      ),
      
      
    );
  }
}
