def muunna_gallonat_litroiksi(gallonat):
    return gallonat * 3,785
gallons = 1
while gallons > 0:
    gallons = float(input("syötä gallonat: "))
    if gallons < 0:
        print(f"{gallons}, galloona on {muunna_gallonat_litroiksi(gallons):.2f}litraa")
if gallons <0:
    print("error: negatiivinen määrä ")