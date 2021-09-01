## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
url = "facebook.com"
een = "1"
nul = "0"
toegestaan = 0

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "drouwens-remote",
    passwd = "Daan04092000.",
    database = "availability-checker"
)

cursor = db.cursor()

if toegestaan == 1:
        cursor.execute("INSERT INTO test VALUES (NULL, %s, %s, %s)", (een, nul, url))
        db.commit()
else:
    print ("Dit is niet toegestaan")


