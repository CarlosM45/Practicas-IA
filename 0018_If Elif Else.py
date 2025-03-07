# If, Elif y Else sirven para crear condiciones bajo las cuales se ejecuta o no una parte del código
galletas = int(input("¿Cuántas galletas vas a regalarme?\n"))
if galletas < 0:  # compara la primera vez
    print("¡Ey!, ¿¿Quieres robarme galletas??\n") # se ejecuta si se cumple la primera condición
elif galletas == 0:  # otra condición en "paralelo"
    print("Tacaño >:(\n")  # se ejecuta si se cumple esta segunda condición,etc
elif galletas == 1:
    print("Yay! 1 galleta\n")
elif 1 < galletas < 10:
    print("Yum!", galletas, "galletas! :3\n")
else:  # si ninguna condición anterior se cumple, se ejecuta esta parte
    print("¿¿Quieres ahogarme en galletas??\n")
