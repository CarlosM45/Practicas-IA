# Ahora aplicaremos if en un ejercicio sencillo para encontrar el mayor número entre 3 entradas del usuario
numero1 = int(input("Ingrese el primer número\n"))
numero2 = int(input("Ingrese el segundo número\n"))
numero3 = int(input("Ingrese el tercer número\n"))
# Asumimos que el primer número es el mayor, por ahora
mayor = numero1
# Ahora verificamos lo anterior, si el segundo número resulta mayor entonces cambiaremos la variable
if numero2 > mayor:
    mayor = numero2
# Y repetimos para nuestro tercer número
if numero3 > mayor:
    mayor = numero3
# Finalmente, imprimimos el número mayor, que no debió haber cambiado si no se cumplieron las condiciones
print("El número mayor es:", mayor)
