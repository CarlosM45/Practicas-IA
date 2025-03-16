# Las listas facilitan el almacenamiento de múltiples valores sin declarar una variable distinta para todos ellos
numeros = [1, 2, 3, 4, 5]
# Puedo mostrar la variable correspondiente lo cual imprimirá toda la lista
print(numeros)
# O elegir un elemento para mostrar
# Python siempre empieza una lista desde la posición 0 para el primer elemento, así que para imprimir 2...
print(numeros[1])
# Se pueden manejar los elementos como uno esperaría, por ejemplo copiando un elemento a otro
numeros[1] = numeros[4]
# Ahora 5 se encuentra 2 veces en la lista
print(numeros)
# El formato por defecto de Python incluye los corchetes para indicar lista, pero también podemos usar bucles para imprimir un elemento a la vez
# Esta vez uso len para definir el rango de for, que recupera la cantidad de elementos de una lista dada
for i in range(len(numeros)):
    print(numeros[i])
