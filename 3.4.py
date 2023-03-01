vuosi = int(input("Anna vuosiluku: "))
if vuosi % 400:
    print(f"Vuosi ", vuosi, "on karkausvuosi.")
else:
    print(f"Vuosi ", vuosi, " ei ole karkausvuosi.")