import configparser
import os
import multiprocessing
from playsound import playsound
import time

os.system ("rm config.ini && wget https://rouwens.ddns.net/muziekservice/config.ini")

config = configparser.ConfigParser()
config.read('config.ini')

def fouteuur (wachtwoord_input, wachtwoord, gebruikersnaam):
    os.system("clear")
    huidige_map = os.system("pwd")
    print ("Selectuur een nummer")
    print ("")
    print ("1 - Vinzzent - Dromendans")
    print ("2 - Rowwen Heze - Bestel maar")
    print ()
    print ("3 - Map downloaden")
    print ("4 - Terug")
    keuze = input()

    if keuze == "1":
        p = multiprocessing.Process(target=playsound, args=("https://rouwens.ddns.net/muziekservice/fouteuur/dromendans.mp3",))
        p.start()
        input("Druk op ENTER om te stoppen")
        p.terminate()
        fouteuur (wachtwoord_input, wachtwoord, gebruikersnaam)

    if keuze == "2":
        p = multiprocessing.Process(target=playsound, args=("https://rouwens.ddns.net/muziekservice/fouteuur/bestelmaar.mp3",))
        p.start()
        input("Druk op ENTER om te stoppen")
        p.terminate()
        fouteuur(wachtwoord_input, wachtwoord, gebruikersnaam)
    
    if keuze == "3":
        cmd = "cd Muziekservice/Fouteuur && wget https://rouwens.ddns.net/muziekservice/fouteuur/dromendans.mp3 && wget https://rouwens.ddns.net/muziekservice/fouteuur/bestelmaar.mp3 && clear"
        os.system(cmd)
        print ("Alle nummers zijn gedownload")
        time.sleep (2)
        fouteuur(wachtwoord_input, wachtwoord, gebruikersnaam)
    
    if keuze == "4":
        menu (wachtwoord_input, wachtwoord, gebruikersnaam)

def volletoeren (wachtwoord_input, wachtwoord, gebruikersnaam):
    os.system("clear")
    print ("Selectuur een nummer")
    print ("")
    print ("1 - Zangeres zonder naam - Mexico")
    print ("2 - De kermisklanten - Hillbilly Rockr")
    print ()
    print ("3 - Map downloaden")
    print ("4 - Terug")
    keuze = input()

    if keuze == "1":
        p = multiprocessing.Process(target=playsound, args=("https://rouwens.ddns.net/muziekservice/volletoeren/mexico.mp3",))
        p.start()
        input("Druk op ENTER om te stoppen")
        p.terminate()
        volletoeren(wachtwoord_input, wachtwoord, gebruikersnaam)

    if keuze == "2":
        p = multiprocessing.Process(target=playsound, args=("https://rouwens.ddns.net/muziekservice/volletoeren/kermisklanten.mp3",))
        p.start()
        input("Druk op ENTER om te stoppen")
        p.terminate()
        volletoeren(wachtwoord_input, wachtwoord, gebruikersnaam)
    if keuze == "3":
        cmd = "cd Muziekservice/Volletoeren && wget https://rouwens.ddns.net/muziekservice/volletoeren/mexico.mp3 && wget https://rouwens.ddns.net/muziekservice/volletoeren/kermisklanten.mp3 && clear"
        os.system(cmd)
        print ("Alle nummers zijn gedownload")
        time.sleep (2)
        volletoeren(wachtwoord_input, wachtwoord, gebruikersnaam)
    
    if keuze == "4":
        menu (wachtwoord_input, wachtwoord, gebruikersnaam)

        

def start ():
    os.system("clear")
    print ("Selecteer het nummer voor je gebruikersnaam")
    print ()
    print ("1 - Daan")
    print ("2 - Esmee")
    gebruikersnaam_input = input()
    os.system("clear")
    print ("Vul je wachtwoord in")
    wachtwoord_input = input()

    if gebruikersnaam_input == "1":
        gebruikersnaam = "daan"

    elif gebruikersnaam_input == "2":
        gebruikersnaam = "esmee"

    gebruikerconfig = "wachtwoord_" + gebruikersnaam
    wachtwoord = config['gebruiker'][gebruikerconfig]
    os.system("clear")

    if wachtwoord_input == wachtwoord:
        menu (wachtwoord_input, wachtwoord, gebruikersnaam)
    
    else:
        print ("Uw wachtwoord klopt niet")

def menu(wachtwoord_input, wachtwoord, gebruikersnaam):
    if wachtwoord_input == wachtwoord:
        os.system("clear")
        print ("Kies een genre")
        print ()
        print ("1 - Foute Uur")
        print ("2 - Op volle toeren")
        genre = input()

        if genre == "1":
            keuze_genre = "fouteuur"
        
        elif genre == "2":
            keuze_genre = "volletoeren"
        
        genre_config = "genre_" + gebruikersnaam
        genre_keuze = config['toegang'][genre_config]
        
        if keuze_genre in genre_keuze:
            if keuze_genre == "fouteuur":
                fouteuur(wachtwoord_input, wachtwoord, gebruikersnaam)
            
            if keuze_genre == "volletoeren":
                volletoeren(wachtwoord_input, wachtwoord, gebruikersnaam)

        else:
            print ("U hebt niet de juiste rechten voor deze genre")
            time.sleep (2)
            menu (wachtwoord_input, wachtwoord, gebruikersnaam)

start()