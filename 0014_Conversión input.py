#Cálculo de una hipotenusa con input y conversiones
cat_a=float(input("Ingrese el valor del primer cateto\n")) # esta línea y la próxima capturan una cadena y la vuelven de tipo float
cat_b=float(input("Ingrese el valor del segundo cateto\n"))
hyp=(cat_a**2+cat_b**2)**0.5 # esta línea calcula la hipotenusa con los catetos float y devolverá otro valor float
print("El valor de la hipotenusa es:",hyp) # imprimir el resultado