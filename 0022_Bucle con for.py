# En el programa anterior, usé un contador para decirle a while cuántas veces ejecutar el bucle. Ese paso lo simplifica for
# Este for se mueve desde 0 a 9 (10 ciclos)
for i in range(10):
    print("El valor de i es:", i)
# Este otro for se mueve desde 2 hasta 7 (6 ciclos), ya que 8 será el primer valor en ser ignorado
for i in range(2, 8):
    print("El valor de i es:", i)
