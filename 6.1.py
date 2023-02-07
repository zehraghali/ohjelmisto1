import random
def heita_noppaa():
    return random.randint(1, 6)
noppa = 0
while noppa !=6:
    noppa = heita_noppaa()
    print(noppa)