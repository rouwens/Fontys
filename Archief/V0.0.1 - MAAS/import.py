import json
import requests
import configparser
import os
import sys
import random
import paramiko
import time
import socket

#config bestand inladen en algemene variabelen toewijzen
config = configparser.ConfigParser()
config.read('config.ini')
download_url = config['default']['download_server'] 
gns3_server = config['default']['gns3_server']

#SSH client
ssh = paramiko.SSHClient()
ssh_username = config['default']['ssh_username'] 
ssh_location_private_key = config['default']['ssh_location_private_key']

system = sys.platform

print ()
print ("Wat is de naam van het project dat je wilt importeren? Vul hier niet de bestandsextentie in")
print ("Voor een compleet overzicht ga je naar http://" + download_url + "/projects")
project_name = input ()

#Download locatie bepalen doormiddel van het systeem
if system == 'win32':
    username = os.getlogin()
    download_path = "'C:\\Users\\" + username + "\Downloads\'"

elif system == 'linux':
    download_path = "~/Downloads/"

#Downloaden van het project
#download_project_url = "http://" + download_url + "/projects/" + project_name + ".gns3project"
#local_file = download_path + project_name + ".gns3project"
#data = requests.get(download_project_url)
#with open(local_file, 'wb')as file:
#    file.write(data.content)

#Het eerste gedeelte van het project ID genereren
id_first_part = str (random.randint(00000000, 99999999))
id = (id_first_part + "-0405-0607-0809-0a0b0c0d0e0f")
payload = {
    "name": "Daan",
    "project_id": id
}

#API request om het project aan te maken uitvoeren.
headers = {'content-type': 'application/json'}
url = "http://" + gns3_server + ":3080/v2/projects"
r = requests.post(url, json=payload, headers=headers)
print (r.text)

cmd = "cd /var/www/projects/ && curl -X POST -H 'Content-type: application/octet-stream' --data-binary @" + project_name + ".gns3project  http://" + gns3_server + ":3080/v2/projects/" + id + "/import"
print (cmd)

if system == 'win32':
    k = paramiko.RSAKey.from_private_key_file(ssh_location_private_key)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=gns3_server, username=ssh_username, pkey=k)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    print(ssh_stdout.read().decode())

elif system == 'linux':
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(gns3_server, username=ssh_username,
        key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa.windows"))
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    print(ssh_stdout.read().decode())

