kaupungit = [ ]
kaupunki = input("Anna seuraava kaupunki: ")
while kaupunki != "":
    kaupungit.append(kaupunki)
    kaupunki = input("Anna seuraava kaupunki: ")
for kaupunki in kaupungit:
    print(kaupunki)