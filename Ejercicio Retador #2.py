# Ejercicio Retador #2 Índices y listas

# se creal las variables y una lista para almazenar los datos

lista_mun = []
total_poblacion = 0
promedio_poblacion = 0.0

# se crea un bucle para preguntar 3 veces por el municipio
i = 0
while i < 3:

    municipio = input("ingresa un municipio: ")
    poblacion = input("ingresa su poblacion: ")
    print("\n")

    lista_mun.append([municipio, poblacion])
    i += 1

# se crea un bucle para sacar el total de la poblacion
i = 0
while i < 3:
    total_poblacion += int(lista_mun[i][1])
    i += 1

# se saca el promedio con el total dividio entre 3
promedio_poblacion = float(total_poblacion) / 3

# se concatena y se imprime
print("El total de la poblacion de los 3 municipios es: " + str(total_poblacion))
print("El promedio de la poblacion es: " + str(promedio_poblacion))
