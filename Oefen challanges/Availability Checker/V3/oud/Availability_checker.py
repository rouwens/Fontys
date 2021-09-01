import os
import time
import mysql.connector as mysql
import datetime


def func_ping(url):

    een = "1"
    nul = "0"
    timer = 5
    ping = os.system("ping -c 1 {0}".format(url))
    
    date_full = datetime.datetime.now()
    date = date_full.strftime("%x")

    db = mysql.connect(
        host = "rouwens.ddns.net",
        user = "drouwens-remote",
        passwd = "Daan04092000.",
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
    func_ping(url)


print ("Vul hier de URL in van de website die je wilt checken op de beschikbaarheid")
url = input()
func_ping(url)


