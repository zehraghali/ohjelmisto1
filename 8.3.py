import mysql.connector
import mysql.connector

yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'root'
    password= 'Zehra,99'
    autocommit=True
    )


def haelentokenttaMaasta(maakoodi):
    sql = SELECT COUNT(type), type FROM airport WHERE iso_country = %sql
    GROUB BY type'''
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql,(maakoodi,))
    tulos = kursori.fetchall()
    return tulos
tyypit = haelentokenttaMaasta(maakoodi)

koodi1 = input("Anna ICAO koodi: ")
koodi2 = input("Anna ICAO koodi: ")
rivi1 = haelentokenttaMaasta(koodi1)
kentta1 =(rivi[4], rivi[5])

rivi2 = haelentokenttaMaasta(koodi2)
kentta2 = (rivi2[4], rivi2[5])

print(distance.distance(kentta1, kentta,)


kentat = haelentokenttaMaasta('FI')
for rivi in kentat:
    print(rivi['name'])
