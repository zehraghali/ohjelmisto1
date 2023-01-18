luku1 = float(input("Anna 1. luku: "))
luku2 = float(input("Anna 2. luku: "))
luku3 = float(input("Anna 3. luku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print(f"Lukujen summa on {summa}, lukujen tulo on {tulo}, lukujen keskiarvo on {keskiarvo: .2f}")