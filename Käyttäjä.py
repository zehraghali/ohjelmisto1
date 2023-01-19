käyttäjä = "python"
salasana = "rules"
kerrat = 0

while kerrat < 5:
    kerrat = kerrat + 1
    print(kerrat)
    user = input("käyttäjätunnus")
    pas = input("salasana")
    if käyttäjä == käyttäjä and salasana == pas:
        print("Tervetuloa")
        break
    else:
     print("Pääsy evätty!")
     print("Kokeile uudestaan")
kerrat = kerrat + 1