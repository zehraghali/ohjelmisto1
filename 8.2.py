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
"SELECt name FROM airport WHERE iso_country =  'FI';"


def haelentokenttaMaasta(maa):
    sql = f"SELECt name FROM airport WHERE iso_country = '{maa}';"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


kentat = haelentokenttaMaasta('FI')
for rivi in kentat:
    print(rivi['name'])
