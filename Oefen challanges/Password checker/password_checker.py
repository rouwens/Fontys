import requests
import string

print ("Vul een wachtwoord in om te checken")
pwd = input()

# Een online woordenlijst met zwakke wachtwoorden die ik online heb gevonden. In de laatste regel van deze snippet word gekeken of het ingvulde 
# wachtwoord in de lijst voorkomst.
pwd_lijst = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/worst-passwords-2017-top100-slashdata.txt') 
x = pwd_lijst.text
find = x.find(pwd)

# In deze list worden alle cijfers inguld. Later word er gekeken of er één van deze cijfers in de string voor komen.
cijfer_list = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
cijfer_list_string = str(cijfer_list)

# De testjes die worden gedaan.
letter_test = not pwd.islower() and not pwd.isupper()
lengte_test = len(pwd)
cijfer_test = any(ele in pwd for ele in cijfer_list_string)
leestekentest = set(string.punctuation)

# Als het wachtwoord niet in de lijst voorkomt dan krijg je als output -1. Als dat wel zo het geval is dan krijg je een getal dat groter is dan 0.
if find > -1:
    print("Het wachtwoord is gevonden in de lijst met onveilige wachtwoorden.")

elif letter_test == False:
    print ("Het wachtwoord bevat geen hoofdletter en/of kleine letter.")

elif lengte_test < 10:
    print ("Het wachtwoord voldoet niet aan de minimale lengte.")

elif cijfer_test == False:
    print("Het wachtwoord heeft geen cijfer(s).")

elif any(str in leestekentest for str in pwd):
    print("Het wachtwoord voldoet aan alle eisen.")

else: 
    print ("Het wachtwoord heeft geen leestekens.")
