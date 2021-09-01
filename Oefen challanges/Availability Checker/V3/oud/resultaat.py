import mysql.connector as mysql
import datetime

db = mysql.connect(
       host = "192.168.178.254",
       user = "drouwens-remote",
       passwd = "Daan04092000.",
       database = "availability-checker"
        )
cursor = db.cursor()

def sqlgelukt(url, strdatum):

    querygelukt = """SELECT SUM(gelukt) FROM data WHERE url = %s AND datum = %s"""
    cursor.execute(querygelukt, (url, strdatum))
    records = cursor.fetchall()
    for record in records:
        var = record
        
    varstr = str(var)
    indexvoor = varstr.index("(") + 1
    indexachter = varstr.index(",") -2
    uitslag = varstr[indexvoor:indexachter]
    print ("Aantal gelukte pings:", uitslag)

def sqlmislukt(url, strdatum):

    querymislukt = """SELECT SUM(mislukt) FROM data WHERE url = %s AND datum = %s"""
    cursor.execute(querymislukt, (url, strdatum))
    records = cursor.fetchall()
    for record in records:
        var = record

    varstr = str(var)
    indexvoor = varstr.index("(") + 1
    indexachter = varstr.index(",") -2
    uitslag = varstr[indexvoor:indexachter] 
    print ("Aantal mislukte pings:", uitslag)

print ("Vul de URL in waarvan je de resultaten wilt zien.")
url = input()

date_full = datetime.datetime.now()
date = date_full.strftime("%x")

print ("Vul hier de datum waarvan de wilt terug kijken van de ping uitslagen")
print ("Gebruik hierbij de volgende tijdsnotatie maand/dag/jaar. Datum van vandaag is: " + date )
datum = input()
strdatum = str(datum)
print ()

sqlgelukt(url, strdatum)
sqlmislukt(url, strdatum)