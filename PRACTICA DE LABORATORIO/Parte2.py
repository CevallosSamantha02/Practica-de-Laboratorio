from Parte1 import *
 
#Gestión de pedidos
pedido = []
total = 0.0
 
while True:
    opcion = input("\nIngrese el nombre del plato que desea (o escriba 'fin' para terminar): ").lower()
   
    if opcion == 'fin':
        break
    elif opcion in menu:
        pedido.append(opcion)
        total += menu[opcion]['precio']
        print(f"> {opcion.title()} añadido correctamente.")
    else:
        print("Ese plato no está en el menú. Intente con otro.")
 
#Pedido final
print("\n Pedido Final:")
for p in pedido:
    print(f"- {p.title()}")
print(f"Total a pagar: ${total}")