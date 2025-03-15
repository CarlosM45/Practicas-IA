# La función range() que alimenta a for también acepta un tercer número entero, que es el incremento deseado de la variable cada ciclo
# Este for por ejemplo sólo imprime el 2 y luego 5, debido al incremento
for i in range(2, 8, 3):
    print("El valor de i es:", i)

# Programa corto cuya tarea es mostrar las primeras potencias de 2
potencia = 1
for expo in range(11):
    print("2 a la potencia", expo, "es", potencia)
    potencia *= 2
