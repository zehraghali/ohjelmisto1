luvut = []

luku = input("Anna ensimmäinen luku, tyhjä lopettaa: ")
while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Anna seuraava luku, tyhjä lopettaa: ")

luvut.sort(reverse=True)
for luku in range(5) :
    print(luvut[luku])