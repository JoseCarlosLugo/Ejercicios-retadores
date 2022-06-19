#Ejercicio Retador #3 Manejo de operadores


cemento = 40
yeso = 30

cantidad_cemento = 0
cantidad_yeso = 0

total_kilos = 0

cantidad_cemento = int(input("cuantos costales de cemento va a comprar: "))
cantidad_yeso = int(input("cuantos costales de yeso va a comprar: "))

print("\n")

total_kilos = (cantidad_cemento * cemento) + (cantidad_yeso * yeso)

if total_kilos > 3254:
  print("El total de kilos es: " + str(total_kilos))
  print("No se puede realizar la compra, exede las carga del transporte")
else:
  print("El total de kilos es: " + str(total_kilos))
  print("compra realizada corectamente")