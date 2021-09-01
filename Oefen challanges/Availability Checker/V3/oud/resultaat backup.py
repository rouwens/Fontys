import mysql.connector as mysql

db = mysql.connect(
       host = "192.168.178.254",
       user = "drouwens-remote",
       passwd = "Daan04092000.",
       database = "availability-checker"
        )
cursor = db.cursor()

def sqlgelukt(url):

    querygelukt = """SELECT SUM(gelukt) FROM data WHERE `url` = %s"""
    cursor.execute(querygelukt, (url,))
    records = cursor.fetchall()
    for record in records:
        var = record
        
    varstr = str(var)
    indexvoor = varstr.index("(") + 1
    indexachter = varstr.index(",") -2
    uitslag = varstr[indexvoor:indexachter]
    print ("Aantal gelukte pings:", uitslag)

def sqlmislukt(url):

    querymislukt = """SELECT SUM(mislukt) FROM data WHERE `url` = %s"""
    cursor.execute(querymislukt, (url,))
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

sqlgelukt(url)
sqlmislukt(url)