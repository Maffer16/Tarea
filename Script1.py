cont = 0
for n in range(0, 1000):
    for d in range(1, n + 1):
      if n % d == 0:
        cont += 1
    if cont == 2:
        print("{}".format(n), end=" ")
    cont = 0
print("Fin")

