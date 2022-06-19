

'''lista_productos = [ID_Pruducto, Proucto, valor]'''
'''venta_productos = [ID_Pruducto, ventas]'''

# Se identifican los elmentos de las listas


lista_productos = [[1, "maiz grano", 285.55], [
    2, "Pepino", 334.72], [3, "tomate verde", 129.00]]

venta_productos = [[2, 122], [1, 89], [1, 22], [3, 48], [1, 75],
                   [3, 322], [2, 95], [1, 148], [1, 83], [3, 100]]

# Se declaran las variables

total_Compra = 0.0
total_maiz = 0
total_pepino = 0
total_tomate = 0
total_ventas = 0
descuento = False

# Se crea un bucle para sumar todas las ventas de la listas "venta_productos "

for elemento_ventas in venta_productos:

    if elemento_ventas[0] == lista_productos[0][0]:
        total_maiz += elemento_ventas[1]

    elif elemento_ventas[0] == lista_productos[1][0]:
        total_pepino += elemento_ventas[1]

    elif elemento_ventas[0] == lista_productos[2][0]:
        total_tomate += elemento_ventas[1]

total_ventas = total_maiz + total_pepino + total_tomate


# Se Crean los input para saber lo que se va a elegir

print("Maiz(1)  Pepino(2)   tomate verde(3) ")
comprar_Producto = int(input("Que producto quieres comprar: "))
Cajas_Producto = int(input("Cuantas cajas va a comprar: "))
print("\n")

# Se suman el total de venta con las cajas que se van a comprar

total_ventas += Cajas_Producto

# Se identifica si Cajas_Producto es mayor a 100 para descuentar el envio
if Cajas_Producto <= 100:
    total_Compra += 1500


# Se identifica el producto a comprar

if comprar_Producto == lista_productos[0][0]:

    # Se calcula el precio de la compra

    total_Compra += (lista_productos[0][2] * Cajas_Producto)

    # Se identifica si El total de cajas vendidas es mayor a 1500
    # Para recibir un descuento de 20%

    if total_ventas >= 1500:

        # Se calcula el descuento

        descuento_resta = (total_Compra * 20) / 100
        total_Compra = total_Compra - descuento_resta
        descuento = True

    # Se muestran los resultados

    print("El producto es: " + str((lista_productos[0][1])))
    print("El precio por caja es: " + str(lista_productos[0][2]))
    print("Se aplica descuento : " + str(descuento))
    print("El costo total a pagar: " + str(total_Compra))


# se repite para los otros productos
elif comprar_Producto == lista_productos[1][0]:

    total_Compra += (lista_productos[1][2] * Cajas_Producto)
    if total_ventas >= 1500:
        descuento_resta = (total_Compra * 20) / 100
        total_Compra = total_Compra - descuento_resta
        descuento = True

    print("El producto es: " + str((lista_productos[1][1])))
    print("El precio por caja es: " + str(lista_productos[1][2]))
    print("Se aplica descuento : " + str(descuento))
    print("El costo total a pagar: " + str(total_Compra))


elif comprar_Producto == lista_productos[2][0]:

    total_Compra += (lista_productos[2][2] * Cajas_Producto)
    if total_ventas >= 1500:
        descuento_resta = (total_Compra * 20) / 100
        total_Compra = total_Compra - descuento_resta
        descuento = True

    print("El producto es: " + str((lista_productos[2][1])))
    print("El precio por caja es: " + str(lista_productos[2][2]))
    print("Se aplica descuento : " + str(descuento))
    print("El costo total a pagar: " + str(total_Compra))


else:
    print("Error")
    print("No existe producto el selecionado")
