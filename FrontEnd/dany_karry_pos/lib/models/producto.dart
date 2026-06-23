class Lomito{
  String tipo;
  int precio;

  Lomito({
    required this.tipo,
    required this.precio
  });
}

void main(){
  Lomito cenaDeHoy = Lomito(tipo: 'Arabe', precio: 28000);
  print(cenaDeHoy.tipo);
  print(cenaDeHoy.precio);
}