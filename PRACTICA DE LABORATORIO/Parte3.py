#Cambios en el menú
from Parte1 import *
 
# Descuento del 15% en la hamburguesa especial
menu['hamburguesa especial']['precio'] *= 0.85
print("\nSe aplicó un descuento en 'Hamburguesa Especial'.")
 
#Plato nuevo del dia
menu['churrasco ecuatoriano'] = {
    'precio': 8.50,
    'ingredientes': ('carne', 'papas fritas', 'ensalada', 'huevo frito')
}
print("Se agregó el 'Churrasco Ecuatoriano' como plato del día.")
 
#Menú actualizado
mostrar_menu(menu)
 
#Especiales del día
especiales = ['ceviche de camarón', 'churrasco ecuatoriano']
print("\n Especiales del Día:")
for plato in especiales:
    datos = menu[plato]
    print(f"{plato.title()} - ${datos['precio']}")