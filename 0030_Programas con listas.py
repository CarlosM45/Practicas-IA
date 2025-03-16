# Ahora que sabemos varios fundamentos de las listas, podemos reescribir un programa de hace unas lecciones: encontrar el número mayor
# Ahora puedo declarar una lista que va a contener todos los números escritos por el usuario, a fin de no sobreescribir la misma variable siempre
lista = []
# Incorporaré también un while con break, como en el programa 24
while True:
    numero = int(input("Ingrese un número, o ingrese -1 para parar\n"))
    if numero == -1:
        break
    lista.append(numero)
# Tan pronto como el usuario rompa el bucle, asumiremos que el primer número es el mayor
mayor = lista[0]
# Compararé todos los números de la lista con for y el uso de in
for numero in lista:
    if numero > mayor:
        mayor = numero
# Ahora puedo regresar varios resultados al usuario, debido al fácil almacenamiento y acceso a la lista
print("Usted ingresó", len(lista), "números")
print("Sus entradas fueron:", lista)
print("El número más grande es:", mayor)
