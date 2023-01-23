laivan_hyttiluokka = input("Laivan hyttiluokka ex: Lux,A,B,C : ")
if laivan_hyttiluokka == "LUX":
    print("parvekkeellinen hytti yläkannella")
elif laivan_hyttiluokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella")
elif laivan_hyttiluokka == "B":
    print("ikkunaton hytti autokannan yläpuolella")
elif laivan_hyttiluokka == "C":
    print("Ikkunaton hytti autokannan alapuolella")
else:
    print("Virheellinen hyttiluokka")