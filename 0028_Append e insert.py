# Usando conocimiento del programa anterior defino una lista, imprimo su longitud y sus elementos
numeros = [1, 2, 3, 4, 5]
print("La lista tiene", len(numeros), "números")
print("Los números son:", numeros)
# La función append añade un nuevo elemento al final de una lista, aumentando también su tamaño en 1
numeros.append(7)
print("La lista ahora tiene", len(numeros), "números")
print("Que son:", numeros)
# La función insert se comporta de forma similar, con la diferencia de que te permite especificar qué posición de la lista tomará el nuevo elemento
numeros.insert(5, 6)
print("Finalmente, la lista tiene", len(numeros), "números")
print("Estos son:", numeros)
