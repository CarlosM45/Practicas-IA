# Como segundo ejemplo del bucle while, se nos pide un código que cuente cuántos números pares e impares introduce el usuario
# Iniciamos 2 contadores en 0
num_par = 0
num_imp = 0
# Leer el primer número
numero = int(input("Ingrese el primer número\n"))
# 0 terminaría el bucle
while numero != 0:
    # Verificamos si el número es par
    if numero % 2 == 0:
        # Aumentamos el contador de pares
        num_par += 1
    # De no cumplir con esa condición, el número sería impar
    else:
        # Aumentamos el contador de impares
        num_imp += 1
    # Leemos el siguiente número
    numero = int(input("Ingrese el siguiente número, o ingrese 0 para parar\n"))
# Cuando pare el bucle, imprimimos los resultados
print("Total de números pares:", num_par)
print("Total de números impares:", num_imp)

# Finalmente, un ejemplo muy sencillo de un bucle que se ejecuta 5 veces exactas, haciendo uso de un contador
contador = 5
while contador != 0:
    print("Dentro del bucle", contador)
    contador -= 1
print("Fuera del bucle")
