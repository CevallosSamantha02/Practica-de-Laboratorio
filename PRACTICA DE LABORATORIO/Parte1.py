#Menú del restaurante
menu = {
    'sandwich mixto': {
        'precio': 3.50,
        'ingredientes': ('pan', 'jamón', 'queso')
    },
    'arroz con pollo': {
        'precio': 5.00,
        'ingredientes': ('arroz', 'pollo', 'guisantes', 'zanahoria')
    },
    'pizza margarita': {
        'precio': 4.25,
        'ingredientes': ('masa', 'salsa de tomate', 'mozzarella', 'albahaca')
    },
    'hamburguesa especial': {
        'precio': 6.75,
        'ingredientes': ('pan', 'carne', 'queso', 'tocino', 'huevo')
    },
    'ceviche de camarón': {
        'precio': 7.00,
        'ingredientes': ('camarón', 'limón', 'cebolla', 'tomate')
    },
    'lasaña': {
        'precio': 6.00,
        'ingredientes': ('pasta', 'carne molida', 'queso', 'salsa de tomate')
    }
}
 
#Mostrar el menú
def mostrar_menu(menu_actual):
    print("\n--- MENÚ RESTAURANTE ---")
    for nombre_plato, info in menu_actual.items():
        print(f"\nPlato: {nombre_plato.title()}")
        print(f"Precio: ${info['precio']}")
        print("Ingredientes:", ', '.join(info['ingredientes']))
 
mostrar_menu(menu)