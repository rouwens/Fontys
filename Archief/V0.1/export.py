import cmd
import configparser
import argparse
import mysql.connector as mysql
import re
import requests
import os
import os.path
import paramiko

ssh = paramiko.SSHClient()

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
    print ("Wat is de naam van het project dat je wilt exporteren?")
    project_name = input()

getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
cursor.execute(getprojectname, (project_name, ))
fetch = cursor.fetchall()
clean = str(fetch)
sql_projectname = re.sub(r'[^\w\s]', '', clean)

#Als de projectnaam bestaat word het het exporteren uitgevoerd
if project_name == sql_projectname:
    getprojectid = """SELECT project_id FROM `projects` WHERE `name` = %s"""
    cursor.execute(getprojectid, (project_name, ))
    fetch = cursor.fetchall()
    clean = str(fetch)
    project_id = clean[3:-4]

    cmd = "curl http://" + gns3_server + ":3080/v2/projects/" + project_id + "/export -o /mnt/" + project_name + ".gns3project" 

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(gns3_server, username=ssh_username,
                key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa"))
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    print(ssh_stdout.read().decode())

else:
    print ("Het project bestaat niet of is niet via deze tool aangemaakt")

#DB verbinding verbreken
cursor.close()
db.close()