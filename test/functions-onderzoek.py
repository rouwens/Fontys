import argparse
import os
start = True

parser = argparse.ArgumentParser(description="Test")
parser.add_argument("-o", "--optie", help="Optie", required=False, default="")

argument = parser.parse_args()
status = False

def message(input_message):
    os.system("Clear")
    if input_message == "":
        print ("Type een bericht en druk op enter")
        input_message = input()
    
    os.system("clear")
    print (input_message)
    exit()

def arguments (option):
    if option == "1":
        message(input_message="Deze tekst zie je omdat je gebruik hebt gemaakt van een paramter")
    
    else:
        message(input_message="Optie niet herkend")

if argument.optie:
    status = True

while start == True:
    if status == True:
        option = argument.optie
        arguments(option)

    os.system("clear")
    print ("Kies een optie")
    print ("")
    print ("1 - Bericht uitprinten")
    print ()
    print ("Vul een nummer in")
    answer = input ()

    if answer == "1":
        message (input_message="")
    else:
        message(input_message="Optie niet herkend")