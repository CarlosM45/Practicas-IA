#Para finalizar un bucle prematuramente o saltar una parte del mismo, Python tiene break y continue a nuestra disposición
#Bucle con break si el usuario escribe "Python"
while True:
    lenguaje=input("¿Cuál es el mejor lenguaje de programación?\n")
    if lenguaje=="Python":
        print("Cierto")
        break
print("Eres libre, por ahora")
#Bucle con continue si el usuario no escribe "Python"
lenguaje=input("¿Cuál es el mejor lenguaje de programación?\n")
while lenguaje!="Python":
    