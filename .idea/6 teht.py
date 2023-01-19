import math
import random

N = int(input("Arvottavien pisteiden määrä: "))
n = 0

arvottujaPisteitä = 0
while arvottujaPisteitä < N:
    x= random.uniform (-1,1)
    y = random.uniform (-1,1)
    if x * x + y * y < 1:
        n += 1
    arvottujaPisteitä += 1

piinlikiarvo = 4 * n / n / N
print(f'Piin likiarvo on {4 * n / N}')
print(f'Piin tarkka arvo on {math.pi}) ja erotus on {piinlikiarvo - math.pi} ')

