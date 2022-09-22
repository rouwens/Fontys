import configparser
import argparse
import mysql.connector as mysql
import random
import re
import requests
import os

parser = argparse.ArgumentParser(description = "GNS3 Project Tool")
parser.add_argument("-p", "--projectnaam", help = "Naam van het project", required = False, default = "")
parser.add_argument("-i", "--projectimport", help = "Naam van het project dat geimporteerd moet worden", required = False, default = "")
parser.add_argument("-b", "--bevesteging", help = "Bevestiging", required = False, default = "")

argument = parser.parse_args()
status = False

if argument.projectnaam:
    status = True
    project_name = argument.projectnaam

if argument.projectimport:
    status = True
    project_import = argument.projectimport

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

if argument.projectimport == "":
    print ("Wat is de naam van het project dat je wilt importeren?")
    project_import = input()

id_first_part = str (random.randint(10000000, 99999999))
project_id = (id_first_part + "-0405-0607-0809-0a0b0c0d0e0f")

payload = {
    "name": project_name,
    "project_id": project_id
}

#Project aanmaken in GNS3
#headers = {'content-type': 'application/json'}
#url = "http://" + gns3_server + ":3080/v2/projects"
#r = requests.post(url, json=payload, headers=headers)
#print (r.text)

#Project importen in GNS3

cmd = "curl -X POST -H 'Content-type: application/octet-stream' --data-binary @" + project_import + ".gns3project http://" + gns3_server + ":3080/v2/projects/" + project_id + "/import?name=" + project_name
os.system = (cmd)
print (cmd)

#project_file = project_import + ".gns3project"
#upload_file = {'upload_file': open(project_file,'rb')}
#url = "http://" + gns3_server + ":3080/v2/projects/" + project_id + "/import"
#r = requests.post(url, files=upload_file,)


#Project naam en ID wegschrijven naar de database
cursor.execute("INSERT INTO `projects` VALUES (NULL, %s, %s)", (project_name, project_id))
db.commit()


#DB verbinding verbreken
cursor.close()
db.close()