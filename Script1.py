cont = 0
inicio = int (input("Número inicial:"))
fin = int (input("Número final:"))
for n in range(inicio, fin):
    for d in range(1, n + 1):
      if n % d == 0:
        cont += 1
    if cont == 2:
        print("{}".format(n), end=" ")
    cont = 0
print("Fin")

