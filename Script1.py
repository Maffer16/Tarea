cont = 0
inicio = int (input("Número inicial:"))
fiin = int (input("Número final:"))
for n in range(inicio, final):
    for d in range(1, n + 1):
      if n % d == 0:
        cont += 1
    if cont == 2:
        print("{}".format(n), end=" ")
    cont = 0
print("Fin")

