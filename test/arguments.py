import argparse

parser = argparse.ArgumentParser(description = "GNS3 Project Tool")
parser.add_argument("-p", "--project", help = "Naam van het project", required = False, default = "")
parser.add_argument("-b", "--bevesteging", help = "Bevestegeging", required = False, default = "")

argument = parser.parse_args()
status = False

if argument.project:
    status = True
    project = argument.project

if argument.bevesteging:
    status = True
    bevesteging = argument.bevesteging

if not status:
    print("Je hebt niks ingevuld") 

if argument.bevesteging == "":
    print ("Wat is de naam van het project?")
    project = input()

if argument.bevesteging == "":
    print ("Wil je een bevesteging?")
    bevesteging = input()



print ("Naam van het project: {0}".format(project))
print("Status van bevesteging: {0}".format(bevesteging))