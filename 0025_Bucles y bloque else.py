# Como la función if, while y for también tienen la posibilidad de usar else, pero con resultados muy distintos y curiosos
# While siempre ejecuta else una vez, independientemente de si siquiera se ejecuta
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# Es más fácil observarlo si le damos a while una condición falsa desde el inicio
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# Al contrario, for no aumenta su valor de i antes de ejecutar else
for i in range(5):
    print(i)
else:
    print("else:", i)
# Y si for no se ejecuta, tendremos de nuevo un else presente
i = 117
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
