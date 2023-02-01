nimet = set()
nimet.add("matti")
nimet.add("matti")
for n in nimet:
    if(n == "matti"):
        print("on jo")
    else:
        print("uusi")
print(nimet.__contains__("matti"))