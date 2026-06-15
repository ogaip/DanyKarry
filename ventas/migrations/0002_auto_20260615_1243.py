# ventas/migrations/0002_cargar_menu_dany_karry.py
from django.db import migrations

def cargar_menu_inicial(apps, schema_editor):
    Producto = apps.get_model('ventas', 'Producto')
    
    menu = [
        # --- COMIDA ---
        {"nombre": "Lomito ARABE", "categoria": "COMIDA", "precio": 28000},
        {"nombre": "Lomito Completo", "categoria": "COMIDA", "precio": 25000},
        {"nombre": "Lomito Simple", "categoria": "COMIDA", "precio": 20000},
        {"nombre": "Lomito con Panceta", "categoria": "COMIDA", "precio": 30000},
        {"nombre": "Lomitón Carne o Pollo", "categoria": "COMIDA", "precio": 60000},
        {"nombre": "LOMI DANY", "categoria": "COMIDA", "precio": 35000},
        {"nombre": "Hamburguesa Simple", "categoria": "COMIDA", "precio": 12000},
        {"nombre": "Hamburguesa Completa", "categoria": "COMIDA", "precio": 15000},
        {"nombre": "Hamburguesa Doble", "categoria": "COMIDA", "precio": 30000},
        {"nombre": "Hamburguesa C/ Panceta", "categoria": "COMIDA", "precio": 25000},
        {"nombre": "Chivito", "categoria": "COMIDA", "precio": 45000},
        {"nombre": "Sándwich de Pollo", "categoria": "COMIDA", "precio": 25000},
        {"nombre": "Super Pancho", "categoria": "COMIDA", "precio": 12000},
        {"nombre": "Papa Frita", "categoria": "COMIDA", "precio": 20000},
        {"nombre": "Papa Frita Chica", "categoria": "COMIDA", "precio": 15000},
        
        # --- BEBIDAS ---
        {"nombre": "Coca Cola de 1/2 L.", "categoria": "BEBIDAS", "precio": 10000},
        {"nombre": "Coca Cola de 1 L.", "categoria": "BEBIDAS", "precio": 12000},
        {"nombre": "Coca Cola de 1 1/2 L.", "categoria": "BEBIDAS", "precio": 17000},
        {"nombre": "Coca Cola de 2 L.", "categoria": "BEBIDAS", "precio": 20000},
        {"nombre": "Coca Lata", "categoria": "BEBIDAS", "precio": 8000},
        {"nombre": "Coca Cola personal", "categoria": "BEBIDAS", "precio": 5000},
        {"nombre": "Jugo 1 L.", "categoria": "BEBIDAS", "precio": 15000},
        
        # --- COMBOS ---
        {"nombre": "Combo: Hamburguesa + Papas Fritas", "categoria": "COMBOS", "precio": 22000},
        {"nombre": "Combo: Lomito Árabe + Papas Fritas", "categoria": "COMBOS", "precio": 35000},
        {"nombre": "Combo: Hamburguesa Completa + Papas + Coca 250ml", "categoria": "COMBOS", "precio": 27000},
        {"nombre": "Combo: Super Pancho + Papas Fritas", "categoria": "COMBOS", "precio": 17000},
        {"nombre": "Combo: Sándwich de Lomito + Papas Fritas", "categoria": "COMBOS", "precio": 32000},
        {"nombre": "Combo Familiar: 5 Hamburguesas Completas + 1 Coca 1 1/2 L.", "categoria": "COMBOS", "precio": 85000},
    ]
    
    for item in menu:
        Producto.objects.create(**item)

def eliminar_menu_inicial(apps, schema_editor):
    Producto = apps.get_model('ventas', 'Producto')
    Producto.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'), # Reemplazá por el nombre exacto de tu primera migración si varía
    ]

    operations = [
        migrations.RunPython(cargar_menu_inicial, eliminar_menu_inicial),
    ]