# Ejercicio Retador #1 Funciones y operaciones básicas en Python

# se declaran las variables con la informacion del pdf
superficie_Sinaloa_km2 = 57365
climas_Sinaloa = ["calido", "subhumedo", "seco", "semiseco"]
temperatura_celsius = 25.45
precipitacion_anual_mm = 790.1

poblacion_m = 1532128
poblacion_h = 1494815
munc_1ro_Cln = 33.15
munc_2do_Mzn = 16.57

# se declaran nuevas variables para la suma de las anteriores
poblacion_T = poblacion_h + poblacion_m
porsentajeT_MZ_Cln = munc_1ro_Cln + munc_2do_Mzn

# se imprime la informacion concatenando

print("La poblacion total de sinaloa es: " + str(poblacion_T))

# se unsa \n para un salto de linea

print("\n")

print("municipios con mas habitantes son Culiacan y Mazatlan con un porsentaje de el " +
      str(porsentajeT_MZ_Cln) + "%")

# se unsa \n para un salto de linea

print("\n")

#

print("La temperatura anual de Sinaloa es" + str(temperatura_celsius) +
      "°C" + " y los tipos de clima son " + ", ".join(climas_Sinaloa))
