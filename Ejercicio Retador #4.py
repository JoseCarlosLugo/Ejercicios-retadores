

'''lista_productos = [ID_Pruducto, Proucto, valor]'''


lista_productos = [[1,"maiz grano",285.55],[2, "Pepino",334.72],[3, "tomate verde", 129.00]]


total_Compra = 0.0

print("Maiz(1)  Pepino(2)   tomate verde(3) ")
comprar_Producto = int(input("Que producto quieres comprar: "))
Cajas_Producto = int(input("Cuantas cajas va a comprar: "))
print("\n")


if Cajas_Producto <= 100:
  total_Compra += 1500

  
if comprar_Producto == lista_productos[0][0]:
  
  total_Compra += (lista_productos[0][2] * Cajas_Producto)
  
  
  print("El producto es: "+ str((lista_productos[0][1])))
  print("El precio por caja es: " + str(lista_productos[0][2]))
  print("El costo total a pagar: " + str(total_Compra))
  

  
  
elif comprar_Producto == lista_productos[1][0]:
  
  total_Compra += (lista_productos[1][2] * Cajas_Producto)
  
  print("El producto es: "+ str((lista_productos[1][1])))
  print("El precio por caja es: " + str(lista_productos[1][2]))
  print("El costo total a pagar: " + str(total_Compra))

elif comprar_Producto == lista_productos[2][0]:
  total_Compra += (lista_productos[2][2] * Cajas_Producto)
  
  print("El producto es: "+ str((lista_productos[2][1])))
  print("El precio por caja es: " + str(lista_productos[2][2]))
  print("El costo total a pagar: " + str(total_Compra))

else:
  print("Error")
  print("No existe producto el selecionado")
  