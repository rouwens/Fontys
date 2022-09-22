import configparser
import random
import requests
import mysql.connector as mysql
import re
import argparse
import platform
import os
import time

def start():

    sleepcounter = 2
    start = "on"
    create = "off"

    # Bepalen van schoonmaak commando op basis van OS
    sys = platform.system()

    if sys == "Windows":
        clear = "cls"

    elif sys == "Linux" or "Darwin":
        clear = "clear"

    # Config inlezen
    config = configparser.ConfigParser()
    config.read('config.ini')
    gns3_server = config['default']['gns3_server']

    # Database config ophalen
    db = mysql.connect(
        host = config['database']['host'],
        user = config['database']['user'],
        passwd = config['database']['pwd'],
        database = config['database']['database'],
        )
    cursor = db.cursor()




    while start == "on":
        os.system (clear)
        print ("GNS3 Management Tool")
        print ()
        print ("1 - Lijst met projecten weergeven")
        print ("2 - Project aanmaken")
        print ("3 - Project verwijderen")
        print ("4 - Project exportern")
        print ("5 - Project importern")
        print ("6 - Afsluiten")
        print ()
        print ("Vul het nummer van de optie die je wilt gebruiken.")
        answer = input ()

        if answer == "1":
            print ()
        
        elif answer == "2":
            start = "off"
            create = "on"

        elif answer == "3":
            print ()
        
        elif answer == "4":
            print ()
        
        elif answer == "5":
            print ()
        
        elif answer == "6":
            
            #DB connectie verbreken
            cursor.close()
            db.close()

            os.system (clear)
            print ("Bye, Bye")
            time.sleep (sleepcounter)
            exit ()
        
        elif answer != "1" or "2" or "3" or "4" or "5" or "6":
            os.system (clear)
            print ("Input niet herkend probeer het opnieuw")
            time.sleep (sleepcounter)

        
        while create == "on":
            print ("Optie twee")
            time.sleep (2) 
            print ("Optie twee")
            time.sleep (2) 
            print ("Optie twee")
            time.sleep (2) 
            create = "off"
            start = "on"


start()