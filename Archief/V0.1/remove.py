import configparser
import requests
import mysql.connector as mysql
import sys
import argparse

parser = argparse.ArgumentParser(description = "GNS3 Project Tool")
parser.add_argument("-p", "--projectnaam", help = "Naam van het project", required = False, default = "")
parser.add_argument("-b", "--bevesteging", help = "Bevestiging", required = False, default = "")

argument = parser.parse_args()
status = False

if argument.projectnaam:
    status = True
    project_name = argument.projectnaam

if argument.bevesteging:
    status = True
    conformation = argument.bevesteging

#config bestand inladen en algemene variabelen toewijzen
config = configparser.ConfigParser()
config.read('config.ini')
gns3_server = config['default']['gns3_server']

#DB config inladen
db = mysql.connect(
    host = config['database']['host'],
    user = config['database']['user'],
    passwd = config['database']['pwd'],
    database = config['database']['database'],
    )
cursor = db.cursor()

system = sys.platform
if argument.projectnaam == "":
    print ("Wat is de naam van het project dat je wilt verwijderen?")
    project_name = input()

print()
if argument.bevesteging == "":
    print ("Weet je het zeker? (y/n)")
    conformation = input()

if conformation == "y":

    getprojectid = """SELECT project_id FROM `projects` WHERE `name` = %s"""
    cursor.execute(getprojectid, (project_name, ))
    fetch = cursor.fetchall()
    clean = str(fetch)
    project_id = clean[3:-4]

    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_server + ":3080/v2/projects/" + project_id
    r = requests.delete(url)
    print (r.text)
    
    cursor.execute("DELETE FROM projects WHERE project_id = %s ;", (project_id,))
    db.commit()
    print ("Project is verwijderd...")

elif conformation == "n":
    print ("Taak is afgebroken door de gebruiker")

else:
    print ("Input niet herkend er zijn geen wijzigingen toegepast")

#DB verbinding verbreken
cursor.close()
db.close()