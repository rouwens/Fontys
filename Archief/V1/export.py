import configparser
import argparse
import mysql.connector as mysql
import re
import requests
import os

parser = argparse.ArgumentParser(description = "GNS3 Project Tool")
parser.add_argument("-p", "--projectnaam", help = "Naam van het project", required = False, default = "")

argument = parser.parse_args()
status = False

if argument.projectnaam:
    status = True
    project_name = argument.projectnaam

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
    print ("Wat is de naam van het project dat je wilt exporteren?")
    project_name = input()

getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
cursor.execute(getprojectname, (project_name, ))
fetch = cursor.fetchall()
clean = str(fetch)
sql_projectname = re.sub(r'[^\w\s]', '', clean)

#Als de projectnaam bestaat word het script afgebroken
if project_name == sql_projectname:
    getprojectid = """SELECT project_id FROM `projects` WHERE `name` = %s"""
    cursor.execute(getprojectid, (project_name, ))
    fetch = cursor.fetchall()
    clean = str(fetch)
    project_id = clean[3:-4]

    project_name_file = project_name + ".gns3project"
    url = "http://" + gns3_server + ":3080/v2/projects/" + project_id + "/export"
    response = requests.get(url, allow_redirects=True)
    open(project_name_file, 'wb').write(response.content)

    if response.status_code != 200:
        print ("Het exporteren is mislukt.")
        cmd = "rm " + project_name_file
        os.system (cmd)
    else:
        print ("Het exporteren van het project is gelukt")

else:
    print ("Het project bestaat niet of is niet via deze tool aangemaakt")

#DB verbinding verbreken
cursor.close()
db.close()