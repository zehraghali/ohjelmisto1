import random
arpa = int(input("Anna arpa kuution määrä: "))
i = 0
for i in range( arpa ) :
    heitot = random.randint (1, 6)
    i += heitot
    print("Silmälukujen summa: ",i)


