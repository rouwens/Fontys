import configparser
import random
import requests
import mysql.connector as mysql
import re
import argparse

parser = argparse.ArgumentParser(description = "GNS3 Management Tool")
parser.add_argument("-p", "--projectnaam", help = "Naam van het (nieuwe) project", required = False, default = "")
parser.add_argument("-b", "--bevesteging", help = "Vul de y van ja om de alles te accepteren ", required = False, default = "")

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

if argument.projectnaam == "":
    print ("Wat is de naam van het nieuwe project?")
    project_name = input()

getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
cursor.execute(getprojectname, (project_name, ))
fetch = cursor.fetchall()
clean = str(fetch)
sql_projectname = re.sub(r'[^\w\s]', '', clean)

#Als de projectnaam bestaat word het script afgebroken
if project_name == sql_projectname:
    print ()
    print ("Project bestaat al. Kies een andere naam")
    cursor.close()
    db.close()
    exit ()

if argument.bevesteging == "":
    print ("Weet je het zeker dat je een nieuw project wilt starten met de naam " + project_name + " ? (y/n)")
    conformation = input()

if conformation == "y":

    #Het eerste gedeelte van het project ID genereren
    id_first_part = str (random.randint(10000000, 99999999))
    id = (id_first_part + "-0405-0607-0809-0a0b0c0d0e0f")

    payload = {
        "name": project_name,
        "project_id": id
    }

    #API request om het project aan te maken uitvoeren.
    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_server + ":3080/v2/projects"
    r = requests.post(url, json=payload, headers=headers)
    print (r.text)

    #Project naam en ID wegschrijven naar de database
    cursor.execute("INSERT INTO `projects` VALUES (NULL, %s, %s)", (project_name, id))
    db.commit()


elif conformation == "n":
    print ("Taak is afgebroken door de gebruiker")

else:
    print("Input niet herkend. Er zijn geen wijzigingen uitgevoerd")

#DB verbinding verbreken
cursor.close()
db.close()
