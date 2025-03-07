# El resultado de un input es una cadena de caracteres
anything = input("Dime lo que quieras\n")
# La siguiente parte fallará siempre por ser un cuadrado de caracteres
'''something=anything**2
print("Así que",something,"eh?")'''
# En cambio, podemos especificar un tipo de dato al cual convertir la cadena de datos
numero = int(input("Ingrese un número\n"))
cuadrado = numero**2
print("El cuadrado de", numero, "es:", cuadrado)
