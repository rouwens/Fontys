import os
import time
import mysql.connector as mysql
import datetime
import time

def start():

    def checker():
        def func_ping(url, timer):

            een = "1"
            nul = "0"

            inttimer = int(timer)
            timer = inttimer
            ping = os.system("ping -c 1 {0}".format(url))
            
            date_full = datetime.datetime.now()
            date = date_full.strftime("%x")

            db = mysql.connect(
                host = "rouwens.ddns.net",
                user = "fontys",
                passwd = "E6g2sAnv4FHBB4HB",
                database = "availability-checker"
            )
            cursor = db.cursor()

            if ping == 0:
                cursor.execute("INSERT INTO data VALUES (NULL, %s, %s, %s, %s)", (een, nul, url, date))
                db.commit()

            else:
                cursor.execute("INSERT INTO data VALUES (NULL, %s, %s, %s, %s)", (nul, een, url, date))
                db.commit()

            time.sleep (timer)
            func_ping(url, timer)

        print ("")
        print ("Vul hier de URL in van de website die je wilt checken op de beschikbaarheid")
        url = input()

        print ()
        print ("Hoeveel seconde moet er tussen de pings zitten?")
        timer = input()

        func_ping(url, timer)

    def resultaat():
            
        db = mysql.connect(
            host = "rouwens.ddns.net",
            user = "fontys",
            passwd = "E6g2sAnv4FHBB4HB",
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
        
        print ("")
        print ("Vul de URL in waarvan je de resultaten wilt zien.")
        url = input()

        date_full = datetime.datetime.now()
        date = date_full.strftime("%x")

        print ("")
        print ("Vul hier de datum waarvan de wilt terug kijken van de ping uitslagen")
        print ("Gebruik hierbij de volgende tijdsnotatie maand/dag/jaar. Datum van vandaag is: " + date )
        datum = input()
        strdatum = str(datum)
        print ()

        sqlgelukt(url, strdatum)
        sqlmislukt(url, strdatum)

        print ()
        print ("Nieuwe resultaten bekijken? (j/n)")
        nogeenkeer = input()
        
        if nogeenkeer == "j":
            resultaat()
        
        if nogeenkeer == "n":
            start()


    print ("")
    print ("Toets één van de volgende opties in")
    print ("")
    print ("1 - Website/systeem pingen")
    print ("2 - Resultaten bekijken")
    print()
    print ("3 - stoppen")
    print ("")

    keuze = input()

    if keuze == "1":
        checker()

    if keuze == "2":
        resultaat()
    
    if keuze == "3":
        exit()

    else:
        print ("Verkeerde input. Probeer het opnieuw....")
        time.sleep(3)
        start()
start()