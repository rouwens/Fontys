import configparser
import random
from tracemalloc import Snapshot
import requests
import mysql.connector as mysql
import re
import argparse
import platform
import os
import os.path
import time
import paramiko
import json
from pathlib import Path

# Config inlezen
config = configparser.ConfigParser()
config.read('config.ini')
gns3_server = config['default']['gns3_server']
ssh_username = config['default']['ssh_username']

# Database config ophalen
db = mysql.connect(
    host = config['database']['host'],
    user = config['database']['user'],
    passwd = config['database']['pwd'],
    database = config['database']['database'],
    )
cursor = db.cursor()

sleepcounter = 2
option = ""
start = "on"
title = "GNS3 Management Tool"
ssh = ("ssh " + ssh_username + "@" + gns3_server + " ")

# Bepalen van schoonmaak commando op basis van OS
sys = platform.system()

if sys == "Windows":
    from win32com.shell import shell,shellcon
    clear = "cls"
    home = shell.SHGetFolderPath(0, shellcon.CSIDL_PROFILE, None, 0)
    ssh_private_key = os.path.isfile(home + "\.ssh\id_rsa")

elif sys == "Linux":
    clear = "clear"
    username = os.getlogin()
    ssh_private_key = os.path.isfile("/home/" + username + "/.ssh/id_rsa")
    home = "~"


elif sys == "Darwin":
    clear = "clear"
    username = os.getlogin()
    ssh_private_key = os.path.isfile("/Users/" + username + "/.ssh/id_rsa")
    home = "~"

if ssh_private_key == False:
    os.system(clear)
    print ("Er is geen SSH privé sleutel gevonden. Hierdoor zullen sommige functies niet werken.")
    time.sleep(5)

else:
    print ()
    #ssh = paramiko.SSHClient()
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.connect(gns3_server, username=ssh_username,
    #key_filename=os.path.join(os.path.expanduser(ssh_private_key)))
    #key_filename=os.path.join(os.path.expanduser("%HOMEPATH%"), ".ssh", "id_rsa"))


def message (message_input):
    os.system(clear)
    print (message_input)
    time.sleep(2)

def messagequestion (message_input):
    os.system(clear)
    print (message_input)

def view ():
    os.system(clear)    
    getprojects = """SELECT name, project_id FROM `projects`"""
    cursor.execute(getprojects)
    fetch = cursor.fetchall()
    messagequestion (message_input="Projectnaam     Project ID")
    print ()
    for row in fetch:
        print(row, '\n')

    input("Druk op enter om door te gaan...")

def create ():
    go = "on"
    messagequestion (message_input="Wat is de naam van het nieuwe project?")
    project_name = input()

    getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
    cursor.execute(getprojectname, (project_name, ))
    fetch = cursor.fetchall()
    clean = str(fetch)
    sql_projectname = re.sub(r'[^\w\s]', '', clean)

    #Als de projectnaam bestaat word het script afgebroken
    if project_name == sql_projectname:
        message (message_input="Project bestaat al. Probeer het opnieuw")
        time.sleep (sleepcounter)
        go = "off"

    if go == "on":

        messagequestion (message_input="Weet je het zeker dat je een nieuw project wilt starten met de naam " + project_name + " ? (y/n)")
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
            
            #Project naam en ID wegschrijven naar de database
            cursor.execute("INSERT INTO `projects` VALUES (NULL, %s, %s)", (project_name, id))
            db.commit()
            
            message (message_input="Het project is aangemaakt")

        elif conformation == "n":
            message (message_input="Taak is afgebroken door de gebruiker")

        else:
            message (message_input="Input niet herkend. Er zijn geen wijzigingen uitgevoerd")

        if option != "":
            exit ()

        messagequestion (message_input="Wil je nog een project aanmaken? (y/n)")
        answer = input()
        
        if answer == "y":
            print ()
        
        elif answer == "n":
            print ()
        else:
            message (message_input="Input niet herkend, je word doorgewezen naar het hoofdmenu")

def remove ():
    remove = "on"
    while remove == "on": 
        messagequestion (message_input="Wat is de naam van het project dat je wilt verwijderen?")
        project_name = input()

        getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
        cursor.execute(getprojectname, (project_name, ))
        fetch = cursor.fetchall()
        clean = str(fetch)
        project_name_sql = clean[3:-4]

        if project_name == project_name_sql:

            messagequestion(message_input="Weet je het zeker dat je het project " + project_name + " wilt verwijderen? (y/n)")
            conformation = input()

            if conformation == "y":

                getprojectid = """SELECT project_id FROM `projects` WHERE `name` = %s"""
                cursor.execute(getprojectid, (project_name, ))
                fetch = cursor.fetchall()
                clean = str(fetch)
                project_id = clean[3:-4]

                url = "http://" + gns3_server + ":3080/v2/projects/" + project_id
                requests.delete(url)

                
                cursor.execute("DELETE FROM projects WHERE project_id = %s ;", (project_id,))
                db.commit()
                message (message_input="Project is verwijderd")

            elif conformation == "n":
                message (message_input="Taak is afgebroken door de gebruiker")

            else:
                message (message_input="Input niet herkend er zijn geen wijzigingen toegepast")
            
            if option != "":
                exit ()

            messagequestion (message_input="Wil je nog een project verwijderen? (y/n)")
            answer = input()
            
            if answer == "y":
                print ()
            
            elif answer == "n":
                remove = "off"
            else:
                message (message_input="Input niet herkend, je word doorgewezen naar het hoofdmenu")
                remove == "off"
        else:
            message (message_input="Het project bestaat niet of is niet via deze tool gemaakt. Probeer het opnieuw")
    
def export ():
    export = "on"
    while export == "on":

        messagequestion (message_input="Wat is de naam van het project dat je wilt exporteren?")
        project_name = input()
            
        messagequestion (message_input="Wat is de naam van het export bestand?")
        exportproject_name = input()

        getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
        cursor.execute(getprojectname, (project_name, ))
        fetch = cursor.fetchall()
        clean = str(fetch)
        sql_projectname = re.sub(r'[^\w\s]', '', clean)

        #Als de projectnaam bestaat word het het exporteren uitgevoerd
        if project_name == sql_projectname:
            os.system(clear)
            getprojectid = """SELECT project_id FROM `projects` WHERE `name` = %s"""
            cursor.execute(getprojectid, (project_name, ))
            fetch = cursor.fetchall()
            clean = str(fetch)
            project_id = clean[3:-4]

            cmd = "curl http://" + gns3_server + ":3080/v2/projects/" + project_id + "/export -o /mnt/" + exportproject_name + ".gns3project" 

            #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #ssh.connect(gns3_server, username=ssh_username,
            #            key_filename=os.path.join(os.path.expanduser(ssh_private_key)))
            #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
            #print(ssh_stdout.read().decode())
            

            message (message_input="Het project is gexporteerd")

        else:
            message (message_input="Het project bestaat niet of is niet via deze tool aangemaakt")
        
        messagequestion (message_input="Wil je nog een project exporteren? (y/n)")
        answer = input()
        
        if answer == "y":
            print ()
        
        elif answer == "n":
            print ()
            export = "off"
        else:
            message (message_input="Input niet herkend, je word doorgewezen naar het hoofdmenu")
            export = "off"
    
def imports ():
    imports = "on"
    while imports == "on":
        go = "on"
        messagequestion (message_input="Wat is de naam van het nieuwe project?")
        project_name = input()
    
        getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
        cursor.execute(getprojectname, (project_name, ))
        fetch = cursor.fetchall()
        clean = str(fetch)
        sql_projectname = re.sub(r'[^\w\s]', '', clean)

        #Als de projectnaam bestaat word het script afgebroken
        if project_name == sql_projectname:
            message (message_input="Project bestaat al. Probeer het opnieuw")
            go = "off"
        
        if go == "on":


            messagequestion (message_input="Wat is de naam van het project dat je wilt importeren?")
            project_import = input()

            os.system(clear)
            print ("Nieuwe projectnaam: " + project_name)
            print ("Template: " + project_import)
            print ("")
            print ("Weet je het zeker dat je het project wilt importeren met de volgende gegevens? (y/n)")
            conformation = input ()

            if conformation == "y":
                
                id_first_part = str (random.randint(10000000, 99999999))
                project_id = (id_first_part + "-0405-0607-0809-0a0b0c0d0e0f")

                cmd = "cd /mnt && curl -X POST -H 'Content-type: application/octet-stream' --data-binary @" + project_import + ".gns3project http://" + gns3_server + ":3080/v2/projects/" + project_id + "/import?name=" + project_name

                #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                #ssh.connect(gns3_server, username=ssh_username,
                #            key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa"))
                #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
                #print(ssh_stdout.read().decode())
                
                os.system (ssh + cmd)

                #Project naam en ID wegschrijven naar de database
                cursor.execute("INSERT INTO `projects` VALUES (NULL, %s, %s)", (project_name, project_id))
                db.commit()
                
                message (message_input="Het project is geimporteerd")
                imports = "off"

            if conformation == "n":
                message (message_input="Er zijn geen wijzigingen aangebracht")
                imports = "off"

            else:
                message (message_input="input niet herkend. Probeer het opnieuw")
            
            messagequestion (message_input= "Wil je nog een project exporteren? (y/n)")
            answer = input()
            
            if answer == "y":
                print ()
            
            elif answer == "n":
                print ()
                imports = "off"
            else:
                message (message_input="Input niet herkend, je word doorgewezen naar het hoofdmenu")
                imports = "off"

def snapshot_view(project_id):
    os.system (clear)              
    #API request om snapshots te zien
    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_server + ":3080/v2/projects/" + project_id +"/snapshots"
    r = requests.get(url, headers=headers)
    
    if r.text == "[]":
        message (message_input="Er is zijn snapshots gemaakt voor dit project")
    
    else:
        print (r.text)
        input("Druk op enter om door te gaan...")

def snapshot_create(project_id, project_name):
    message (message_input= "Wat is de naam van de snapshot?")
    answer = input()
    
    payload = {
        "name": answer,
    }

    #API request om de snapshot te maken 
    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_server + ":3080/v2/projects/" + project_id +"/snapshots"
    r = requests.post(url, json=payload, headers=headers)
    data = r.json()
    snapshot_id = data["snapshot_id"]

    #Project naam en ID wegschrijven naar de database
    cursor.execute("INSERT INTO `snapshots` VALUES (NULL, %s, %s, %s)", (project_name, answer, snapshot_id))
    db.commit()

    message (message_input = "De snapshot is gemaakt")

def snapshot_remove(project_id, project_name):
    message (message_input="Wat is de naam van de snapshot dat je wilt verwijderen?")
    answer = input()

    message (message_input="Weet je het zeker dat je de snapshot " + answer + " wilt verwijderen (y/n)")
    conformation = input()

    if conformation == "y":
        #Snapshot ID ophalen uit de database
        getsnapshotid = """SELECT snapshot_id FROM `snapshots` WHERE `project_name` = %s AND `snapshot_name` = %s"""
        cursor.execute(getsnapshotid, (project_name, answer ))
        fetch = cursor.fetchall()
        clean = str(fetch)
        snapshot_id = clean[3:-4]

        #Snapshot naam ophalen uit de database
        getsnapshotname = """SELECT snapshot_name FROM `snapshots` WHERE `project_name` = %s AND `snapshot_name` = %s"""
        cursor.execute(getsnapshotname, (project_name, answer ))
        fetch = cursor.fetchall()
        clean = str(fetch)
        snapshot_name = clean[3:-4]

        if snapshot_name == answer:
            headers = {'content-type': 'application/json'}
            url = "http://" + gns3_server + ":3080/v2/projects/" + project_id + "/snapshots/" + snapshot_id
            r = requests.delete(url, headers=headers)

            cursor.execute("DELETE FROM snapshots WHERE snapshot_id = %s ;", (snapshot_id,))
            db.commit()
            message (message_input="Snapshot is verwijderd")
        
        else:
            message (message_input="Snapshot is niet gevonden in de database, probeer het opnieuw")
            
        
    elif conformation == "n":
        message(message_input="Taak afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd.")
    else:
        message(message_input="Input niet herkend probeer het opnieuw")

def snapshot_restore(project_id, project_name):
    messagequestion ("Wat is de naam van de snapshot die je wilt herstellen?")
    answer = input ()

    messagequestion("Weet je het zeker dat je snapshot " + answer + " wilt herstellen? (y/n)")
    conformation = input ()

    if conformation == "y":
        #Snapshot ID ophalen uit de database
        getsnapshotid = """SELECT snapshot_id FROM `snapshots` WHERE `project_name` = %s AND `snapshot_name` = %s"""
        cursor.execute(getsnapshotid, (project_name, answer ))
        fetch = cursor.fetchall()
        clean = str(fetch)
        snapshot_id = clean[3:-4]

        headers = {'content-type': 'application/json'}
        url = "http://" + gns3_server + ":3080/v2/projects/" + project_id + "/snapshots/" + snapshot_id + "/restore"
        r = requests.post(url, headers=headers)
        print (r.text)
        time.sleep(10)
        message (message_input="Snapshot is hersteld")
        
    elif conformation == "n":
        message (message_input="Taak is afgebroken door de gebruiker")

    else:
        message (message_input="Input niet herkend. Er zijn geen wijzigingen uitgevoerd")

def snapshot_menu ():
    project_name = ""
    while start == "on":
        go = "on"

        if project_name == "":
            os.system(clear)
            print ("Wat is de naam van het project?")
            project_name = input()

            getprojectname = """SELECT name FROM `projects` WHERE `name` = %s"""
            cursor.execute(getprojectname, (project_name, ))
            fetch = cursor.fetchall()
            clean = str(fetch)
            sql_projectname = re.sub(r'[^\w\s]', '', clean)

            getprojectid = """SELECT project_id FROM `projects` WHERE `name` = %s"""
            cursor.execute(getprojectid, (project_name, ))
            fetch = cursor.fetchall()
            clean = str(fetch)
            project_id = clean[3:-4]

            #API request om het project te openen 
            headers = {'content-type': 'application/json'}
            url = "http://" + gns3_server + ":3080/v2/projects/" + project_id +"/open"
            r = requests.post(url, headers=headers)

            if project_name != sql_projectname:
                os.system(clear)
                print ("Project bestaat niet. Kies een andere naam")
                time.sleep(sleepcounter)
                go = "off"
            
            else:
                go = "on"
        
        if go == "on":
            os.system(clear)
            print ("Snapshots beheren van project " + project_name)
            print ()
            print ("1 - Snapshots weergeven")
            print ("2 - Snapshot maken")
            print ("3 - Snapshot verwijderen")
            print ("4 - Snapshot terug zetten")
            print ("5 - Ander project beheren")
            print ("6 - Terug gaan naar het vorige menu")
            print ("7 - Afsluiten")
            print ()
            print ("Vul het nummer van de optie die je wilt gebruiken.")
            answer = input ()

            if answer == "1":
                snapshot_view(project_id)

            
            elif answer == "2":
                snapshot_create(project_id, project_name)
            
            elif answer == "3":
                snapshot_remove(project_id, project_name)                

            elif answer == "4":
                snapshot_restore(project_id, project_name)
            
            elif answer == "5":
                project_name = ""
            
            elif answer == "6":
                return ()
            
            elif answer == "7":
                afsluiten()
            
            elif answer != "1" or "2" or "3" or "4" or "5" or "6" or "7":
                os.system (clear)
                print ("Input niet herkend probeer het opnieuw")
                time.sleep (sleepcounter)

def manage_checkversion():
    os.system(clear)
    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_server + ":3080/v2/version"
    r = requests.get(url, headers=headers)
    print (r.text)
    print ()
    input("Druk op enter om door te gaan...")

def manage_projects():
    while start == "on":
        os.system(clear)
        print (title)
        print ()
        print ("1 - Project exports weergeven")
        print ("2 - Project export verwijderen")
        print ("3 - Terug gaan")
        print ("4 - Afsluiten")
        answer = input()

        if answer == "1":
            os.system(clear)
            cmd = ssh + "'ls /mnt'"
            command = os.system(cmd)
            print (command)
            #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls /mnt")
            #print(ssh_stdout.read().decode())
            input("Druk op enter om door te gaan...")

        elif answer == "2":
            messagequestion (message_input="Wat is de naam van de template die je wilt verwijderen?")
            answer = input()

            messagequestion (message_input="Weet je het zeker dat je " + answer + " wilt verwijderen? (y/n)")
            conformation = input()

            if conformation == "y":
                cmd = "rm /mnt/" + answer + ".gns3project"
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
                message ("Opdracht is uitgevoerd, check de lijst met projecten om te zien of het project nog bestaat")
                    
            elif conformation == "n":
                message(message_input="Taak afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd.")
            else:
                message(message_input="Input niet herkend probeer het opnieuw")

        elif answer == "3":
            return ()
            
        elif answer == "4":
            afsluiten()

def manage_ssh():
    if sys == "Windows":
        home = str(Path.home())

        cmd = "type $env:USERPROFILE\.ssh\id_rsa.pub | ssh " + ssh_username + "@" + gns3_server + "'cat >> .ssh/authorized_keys'"
        ssh_private_key = os.path.isfile(home + "\.ssh\id_rsa")

    elif sys == "Linux" or "Darwin":
        cmd = "ssh-copy-id " + ssh_username + "@" + gns3_server

        if sys == "Linux":
            username = os.getlogin()
            ssh_private_key = os.path.isfile("/home/" + username + "/.ssh/id_rsa")
        
        elif sys == "Darwin":
            username = os.getlogin()
            ssh_private_key = os.path.isfile("/Users/" + username + "/.ssh/id_rsa")

    if ssh_private_key == True:
        os.system(clear)
    
    if ssh_private_key == False:
        messagequestion ("Er zijn geen SSH sleutels gevonden. Wil je die nu maken? (y/n)")
        answer= input()

        if answer == "y":
            os.sytem(clear) 
            os.system("ssh-keygen")
        
        elif answer == "n":
            message (message_input="Taak is afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd")
            return()

        else:
            message ("Input niet herkend. Probeer het opniew")
            return()

    test = os.system (cmd)
    print (test)
    print (ssh_private_key)
    time.sleep(10)
 
    message(message_input="De SSH sleutel is geimporteerd")

def manage_menu ():
    while start == "on":
        os.system(clear)
        print (title)
        print ()
        print ("1 - GNS3 versie weergeven")
        print ("2 - GNS3 project templates beheren")
        print ("3 - SSH sleutel installeren")
        print ("4 - Terug gaan")
        print ("5 - Afsluiten")
        answer = input()

        if answer == "1":
            manage_checkversion()
        
        elif answer == "2":
            manage_projects()
        
        elif answer == "3":
            manage_ssh()

        elif answer == "4":
            return()
        
        elif answer == "5":
            afsluiten()
        
        elif answer != "1" or "2" or "3" or "4" or "5":
            message (message_input="Input niet herkend probeer het opnieuw")
    

def afsluiten():
        #DB connectie verbreken
        cursor.close()
        db.close()

        os.system (clear)
        print ("Bye, Bye")
        time.sleep (sleepcounter)
        exit ()

while start == "on":       
    os.system (clear)
    print ("GNS3 Management Tool")
    print ()
    print ("1 - Lijst met projecten weergeven")
    print ("2 - Project aanmaken")
    print ("3 - Project verwijderen")
    print ("4 - Project exportern")
    print ("5 - Project importern")
    print ("6 - Snapshot")
    print ("7 - Beheer")
    print ()
    print ("8 - Afsluiten")
    print ()
    print ("Vul het nummer van de optie die je wilt gebruiken.")
    answer = input ()

    if answer == "1":
        view ()

    elif answer == "2":
        create () 

    elif answer == "3":
        remove ()

    elif answer == "4":
        export ()

    elif answer == "5":
        imports ()
    
    elif answer == "6":
        snapshot_menu ()
    
    elif answer == "7":
        manage_menu ()

    elif answer == "8":
        afsluiten()


    elif answer != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8":
        message (message_input="Input niet herkend probeer het opnieuw")