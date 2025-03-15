# Si queremos que el programa anterior continúe indefinidamente, preguntando tantos números al usuario como él quiera, usaremos a while
# Almaceno un número más pequeño que cualquiera que pudiese ingresar el usuario, para inicializar
mayor = -999999
# Pregunto el primer número
numero = int(input("Ingrese el primer número\n"))
# Mientras el número no sea igual a -1, el bucle while continúa
while numero != -1:
    # Comparamos el número con el número mayor
    if numero > mayor:
        # Si es cierto, estableceremos ese número como el nuevo mayor
        mayor = numero
    # Ingresar siguiente número
    numero = int(
        input("Ingrese el siguiente número, o ingrese -1 para parar\n"))
# Fuera del bucle, concluimos imprimiendo el número más grande ingresado durante el programa
print("El número mayor fue:", mayor)
