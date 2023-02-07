import random


def nopanHeitto(eyeInt):
    return random.randint(1, eyeInt)

tahko = int(input("Anna nopan tahkojen määrä: "))
noppa = 0

while noppa != tahko:
    noppa = nopanHeitto(tahko)
    print(noppa)