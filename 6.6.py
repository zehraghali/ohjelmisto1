import math

def yksikkoHinta(halkaisija, hinta):
    sadeSentteina = halkaisija / 2
    sadeMetreina = sadeSentteina / 100
    pintaAla = math.pi * math.pow(sadeMetreina, 2)
    return hinta / pintaAla

pizza_1_halkaisija = float(input("pizza 1 halkaisija: "))
pizza_1_hinta = float(input("Pizza 1 hinta: "))
pizza_2_halkaisija = float(input("pizza 2 halkaisija: "))
pizza_2_hinta = float(input("Pizza 2 hinta"))

pizza1 = yksikkoHinta(pizza_1_halkaisija, pizza_1_hinta)
pizza2 = yksikkoHinta(pizza_2_halkaisija, pizza_2_hinta)

print(pizza1, pizza2)
if (pizza1 < pizza2):
    print("Pizza 1 on yksikköhinnaltaan halvempi")
else:
    print("pizza 2 on yksikköhinnaltaan halvempi")
