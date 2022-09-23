import configparser
import argparse
import mysql.connector as mysql
import random
import os
import os.path
import paramiko

ssh = paramiko.SSHClient()

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
ssh_username = config['default']['ssh_username']

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

if argument.bevesteging == "":
    print ("Weet je het zeker dat je het project wilt importeren met de volgende gegevens? (y/n")
    print ("")
    print ("Nieuwe projectnaam: " + project_name)
    print ("Template: " + [project_import])
    conformation = input ()

if conformation == "y":
    
    #Project importen in GNS3

    id_first_part = str (random.randint(10000000, 99999999))
    project_id = (id_first_part + "-0405-0607-0809-0a0b0c0d0e0f")

    cmd = "cd /mnt && curl -X POST -H 'Content-type: application/octet-stream' --data-binary @" + project_import + ".gns3project http://" + gns3_server + ":3080/v2/projects/" + project_id + "/import?name=" + project_name

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(gns3_server, username=ssh_username,
                key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa"))
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    #print(ssh_stdout.read().decode())

    #Project naam en ID wegschrijven naar de database
    cursor.execute("INSERT INTO `projects` VALUES (NULL, %s, %s)", (project_name, project_id))
    db.commit()

    print ("Het project is geimporteerd")

if conformation == "n":
    print ("Er zijn geen wijzigingen aangebracht")

else:
    print ("input niet herkend. Probeer het opnieuw")

#DB verbinding verbreken
cursor.close()
db.close()