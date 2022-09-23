import configparser
import random
import requests
import mysql.connector as mysql
import re
import argparse
import platform
import os
import os.path
import time
import paramiko

ssh = paramiko.SSHClient()

parser = argparse.ArgumentParser(description = "GNS3 Management Tool")
parser.add_argument("-o", "--optie", help = "Opties: aanmaken, verwijderen, exporteren, importeren", required = False, default = "")
parser.add_argument("-p", "--projectnaam", help = "Naam van het (nieuwe)project", required = False, default = "")
parser.add_argument("-ex", "--exportnaam", help = "Naam van het export project", required = False, default = "")
parser.add_argument("-pi", "--projectimport", help = "Naam van het project dat geimporteerd moet worden", required = False, default = "")
parser.add_argument("-b", "--bevesteging", help = "Bevestiging", required = False, default = "")


argument = parser.parse_args()
status = False

if argument.optie:
    status = True
    option = argument.optie

if argument.projectnaam:
    status = True
    project_name = argument.projectnaam

if argument.exportnaam:
    status = True
    newproject_name = argument.exportnaam

if argument.projectimport:
    status = True
    project_import = argument.projectimport

if argument.bevesteging:
    status = True
    conformation = argument.bevesteging

sleepcounter = 2
option = ""
start = "on"

# Bepalen van schoonmaak commando op basis van OS
sys = platform.system()

if sys == "Windows":
    clear = "cls"

elif sys == "Linux" or "Darwin":
    clear = "clear"

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

def create ():
    go = "on"
    os.system(clear)
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
        os.system(clear)
        print ("Project bestaat al. Probeer het opnieuw")
        time.sleep (sleepcounter)
        go = "off"

    if go == "on":

        os.system(clear)
                        
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
            
            #Project naam en ID wegschrijven naar de database
            cursor.execute("INSERT INTO `projects` VALUES (NULL, %s, %s)", (project_name, id))
            db.commit()
            
            os.system(clear)
            print ("Het project is aangemaakt")
            time.sleep(sleepcounter)

        elif conformation == "n":
            os.system(clear)
            print ("Taak is afgebroken door de gebruiker")
            time.sleep(sleepcounter)

        else:
            os.system(clear)
            print("Input niet herkend. Er zijn geen wijzigingen uitgevoerd")
            time.sleep(sleepcounter)

        os.system (clear)
        if option != "":
            exit ()
        print ("Wil je nog een project aanmaken? (y/n)")
        answer = input()
        
        if answer == "y":
            print ()
        
        elif answer == "n":
            print ()
        else:
            os.system(clear)
            print ("Input niet herkend, je word doorgewezen naar het hoofdmenu")
            time.sleep(sleepcounter)

def remove ():
    remove = "on"
    while remove == "on": 
        if argument.projectnaam == "":
            os.system (clear)
            print ("Wat is de naam van het project dat je wilt verwijderen?")
            project_name = input()

        print()
        if argument.bevesteging == "":
            os.system(clear)
            print ("Weet je het zeker dat je het project " + project_name + " wilt verwijderen? (y/n)")
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
            #print (r.text)
            
            cursor.execute("DELETE FROM projects WHERE project_id = %s ;", (project_id,))
            db.commit()
            os.system(clear)
            print ("Project is verwijderd...")
            time.sleep (sleepcounter)

        elif conformation == "n":
            os.system(clear)
            print ("Taak is afgebroken door de gebruiker")
            time.sleep(sleepcounter)

        else:
            os.system(clear)
            print ("Input niet herkend er zijn geen wijzigingen toegepast")
            time.sleep (sleepcounter)
            os.system (clear)
        
        if option != "":
            exit ()

        os.system(clear)    
        print ("Wil je nog een project verwijderen? (y/n)")
        answer = input()
        
        if answer == "y":
            print ()
        
        elif answer == "n":
            remove = "off"
        else:
            os.system(clear)
            print ("Input niet herkend, je word doorgewezen naar het hoofdmenu")
            time.sleep(sleepcounter)
            remove == "off"
    
def export ():
    export = "on"
    while export == "on":
        os.system (clear)
        if argument.projectnaam == "":
            print ("Wat is de naam van het project dat je wilt exporteren?")
            project_name = input()
            
        
        if argument.exportnaam == "":
            os.system(clear)
            print ("Wat is de naam van het export bestand?")
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

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(gns3_server, username=ssh_username,
                        key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa"))
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
            print(ssh_stdout.read().decode())
            
            os.system(clear)
            print ("Het project is gexporteerd")
            time.sleep (sleepcounter)

        else:
            os.system(clear)
            print ("Het project bestaat niet of is niet via deze tool aangemaakt")
            time.sleep(sleepcounter)
        
        os.system(clear)    
        print ("Wil je nog een project exporteren? (y/n)")
        answer = input()
        
        if answer == "y":
            print ()
        
        elif answer == "n":
            print ()
            export = "off"
        else:
            os.system(clear)
            print ("Input niet herkend, je word doorgewezen naar het hoofdmenu")
            time.sleep(sleepcounter)
            export = "off"
    
def imports ():
    imports = "on"
    while imports == "on":
        go = "on"
        os.system(clear)
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
                os.system(clear)
                print ("Project bestaat al. Probeer het opnieuw")
                time.sleep (sleepcounter)
                go = "off"
        
        if go == "on":

            if argument.projectimport == "":
                os.system (clear)
                print ("Wat is de naam van het project dat je wilt importeren?")
                project_import = input()

            if argument.bevesteging == "":
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

                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(gns3_server, username=ssh_username,
                            key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa"))
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
                #print(ssh_stdout.read().decode())

                #Project naam en ID wegschrijven naar de database
                cursor.execute("INSERT INTO `projects` VALUES (NULL, %s, %s)", (project_name, project_id))
                db.commit()
                
                os.system(clear)
                print ("Het project is geimporteerd")
                time.sleep(sleepcounter)
                imports = "off"

            if conformation == "n":
                os.system(clear)
                print ("Er zijn geen wijzigingen aangebracht")
                time.sleep(sleepcounter)
                imports = "off"

            else:
                os.system(clear)
                print ("input niet herkend. Probeer het opnieuw")
                time.sleep(sleepcounter)
            
            os.system(clear)    
            print ("Wil je nog een project exporteren? (y/n)")
            answer = input()
            
            if answer == "y":
                print ()
            
            elif answer == "n":
                print ()
                imports = "off"
            else:
                os.system(clear)
                print ("Input niet herkend, je word doorgewezen naar het hoofdmenu")
                time.sleep(sleepcounter)
                imports = "off"

            
while start == "on":       
    os.system (clear)
    print ("GNS3 Management Tool")
    print ()
    print ("1 - Lijst met projecten weergeven")
    print ("2 - Project aanmaken")
    print ("3 - Project verwijderen")
    print ("4 - Project exportern")
    print ("5 - Project importern")
    print ("6 - Afsluiten")
    print ()
    print ("Vul het nummer van de optie die je wilt gebruiken.")
    answer = input ()

    if answer == "1":
        print ()

    elif answer == "2":
        create () 

    elif answer == "3":
        remove ()

    elif answer == "4":
        export ()

    elif answer == "5":
        imports ()

    elif answer == "6":
        
        #DB connectie verbreken
        cursor.close()
        db.close()

        os.system (clear)
        print ("Bye, Bye")
        time.sleep (sleepcounter)
        exit ()

    elif answer != "1" or "2" or "3" or "4" or "5" or "6":
        os.system (clear)
        print ("Input niet herkend probeer het opnieuw")
        time.sleep (sleepcounter)