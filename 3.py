sukupuoli = input("kirjoita sukupuolesi (mies/nainen): ")
hemoglobiini = int(input("Kirjoita heoglobiiniarvosi: "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        tulos = "alhainen"
    elif 117 <= hemoglobiini <= 175:
        tulos = "normaali"
    else:
        tulos = "korkea"
else:
    if hemoglobiini < 134:
        tulos = "alhainen"
    elif 134 <= hemoglobiini <= 195:
        tulos = "normaaali"
    else:
        tulos = "korkea"
print("Hemoglobiinisi on "+tulos)

