from ldap3 import Server, Connection, ALL
import time

server =Server('192.168.195.144', get_info=ALL)
conn = Connection(server, 'cn=admin,dc=rouwens,dc=com', 'welkom01', auto_bind=True)

#conn.add('cn=Lieke Rouwens,ou=gebruikers,dc=rouwens,dc=com', 'inetOrgPerson', {'givenName': 'Lieke', 'sn': 'Rouwens', 'uid': 'lrouwens', 'userPassword': 'welkom'})

def start():

                def keuze1():

                    print("Voornaam")
                    voornaam = input()
                    print()

                    print("Achternaam")
                    achternaam = input()
                    print()

                    print("Gebruikersnaam")
                    gebruikersnaam = input()
                    print()

                    print("Wachtwoord")
                    wachtwoord1 = str(input())
                    print()

                    print("Wachtwoord ter herhaling") 
                    wachtwoord2 = str(input())
                    print()

                    uid = achternaam + " " + voornaam

                    if wachtwoord1 == wachtwoord2:
                        print ("UID: ", uid)
                        print ("Voornaam: ", voornaam)
                        print ("Achternaam: ", achternaam)
                        print ("Gebruikersnaam: ", gebruikersnaam)
                        print ("Wachtwoord: ", wachtwoord1)
                        print ('')
                        print ("Kloppen deze gegevens? (y/n) ")
                        conf = input()
                        
                        if conf == "y":
                            ldaptest = "'cn=" + uid + ",ou=gebruikers,dc=rouwens,dc=com', 'inetOrgPerson', {'givenName': '" + voornaam "', "  + "'givenName': '" + voornaam + "', "
                            #ldapvoornaam = "'givenName': '" + voornaam + "', "
                            print (ldaptest)
                            #print ("conn.add('cn="uid",ou=gebruikers,dc=rouwens,dc=com', 'inetOrgPerson', {'givenName': 'Lieke', 'sn': 'Rouwens', 'uid': 'lrouwens', 'userPassword': 'welkom'}))


                        time.sleep(3)
                        start()

                    else:
                        print ("Wachtwoord klopt niet")               


                    start()

                def Keuze2():
                    print("Keuze 2 gekozen")
                    start()
                def keuze3():
                    print("Keuze 3 gekozen")
                    start()
                
                print ("LDAP gebruikers beheren")
                print ("")
                print ("Toets 1 om een gebruiker aan te maken")
                print ("Toets 2 om een gebruiker aan te passen")
                print ("Toets 3 om een gebruiker te verwijderen")
                print ("")
                keuze = input()


                if keuze == "1":
                   keuze1()
            
                elif keuze == "2":
                    print("Keuze2")
            
                elif keuze == "3":
                    print("Keuze3")
                
                elif keuze == "exit":
                    exit()
                    
                else:
                    print ("Verkeerde input. Probeer het opnieuw....")
                    time.sleep(1)
                start()

start()