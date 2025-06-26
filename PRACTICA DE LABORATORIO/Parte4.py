#Exploración de errores
from Parte1 import menu, pedido  # Importamos solo lo necesario

# 1. Error de índice fuera de rango (IndexError)
print("\n IndexError")
try:
    # Intentamos acceder a un índice que no existe en la lista de pedidos
    print(pedido[10])
except IndexError as e:
    print(f"Error: {e}")

# 2. Error por clave inexistente en el diccionario (KeyError)
print("\n KeyError")
try:
    # Buscamos un plato que no existe en el menú
    print(menu['pizza napolitana'])
except KeyError as e:
    print(f"Error: {e}")

# 3. Error por modificar una tupla (TypeError)
print("\n TypeError")
try:
    # Intentamos cambiar un ingrediente dentro de una tupla (que es inmutable)
    menu['lasagna']['ingredientes'][0] = 'pollo'
except TypeError as e:
    print(f"Error: {e}")

# Fin de la exploración de errores
print("\n Fin de la Parte 4: Exploración de errores.")