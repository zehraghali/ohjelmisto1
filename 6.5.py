luvut = [1, 34, 4, 5, 6, 7, 8, 987, 11, 12, 880, 14, 15]

def parilliset(kokonais):
    parillisetluvut = []
    for luku in kokonais:
        if luku % 2  == 0:
            parillisetluvut.append(luku)
    return kokonais
tulos = parilliset(luvut)
print(luvut)
print(tulos)