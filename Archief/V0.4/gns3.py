import configparser
import random
from tracemalloc import Snapshot
import requests
import re
import argparse
import platform
import os
import os.path
import time
import paramiko
import json
import pandas as pd

# Config inlezen
config = configparser.ConfigParser()
config.read('config.ini')
gns3_server = config['default']['gns3_server']
ssh_username = config['default']['ssh_username']

template_cloud = config['templates']['cloud']
template_fortigate = config['templates']['fortigate']
template_switch = config['templates']['switch']
template_pc = config['templates']['pc']

sleepcounter = 2
option = ""
start = "on"
title = "GNS3 Management Tool"
ssh = ("ssh " + ssh_username + "@" + gns3_server + " ")
clear = ("clear")

def message (message_input):
    os.system(clear)
    print (message_input)
    time.sleep(2)

def messagequestion (message_input):
    os.system(clear)
    print (message_input)

def view ():
    os.system(clear)
    headers = {'content-type': 'application/json'}
    url = f"http://{gns3_server}:3080/v2/projects"
    r = requests.get(url, headers=headers)
    data = r.json()

    df = pd.DataFrame.from_dict(data)
    print(df[['name', 'project_id']])   

def create ():
    go = "on"
    messagequestion (message_input="Wat is de naam van het nieuwe project?")
    project_name = input()

    os.system("clear")
    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_server + ":3080/v2/projects"
    r = requests.get(url, headers=headers)
    data = r.json()

    items = []
    for item in data:
        items.append(item['name'])

    #Als de projectnaam bestaat word het script afgebroken
    if project_name in items:
        message (message_input="Project bestaat al. Probeer het opnieuw")
        time.sleep (sleepcounter)
        go = "off"

    if go == "on":

        messagequestion (message_input="Weet je het zeker dat je een nieuw project wilt starten met de naam " + project_name + " ? (y/n)")
        conformation = input()

        if conformation == "y":

            #Het eerste gedeelte van het project ID genereren
            id_first_part = str (random.randint(10000000, 99999999))
            project_id = f"{id_first_part}-0405-0607-0809-0a0b0c0d0e0f"

            payload = {
                "name": project_name,
                "project_id": project_id
            }

            #API request om het project aan te maken uitvoeren.
            headers = {'content-type': 'application/json'}
            url = "http://" + gns3_server + ":3080/v2/projects"
            r = requests.post(url, json=payload, headers=headers)
            
            message (message_input="Het project is aangemaakt")

            messagequestion (message_input="Wil je apparaten toevoegen aan je nieuwe project? (y/n)")
            answer_add_devices = input()

            if answer_add_devices == "y":
                add_devices(project_id)
            
            elif answer_add_devices == "n":
                message (message_input="Je word doorgewezen naar het hoofdmenu")
                return()
            
            else:
                message(message_input="Input niet herkend. Je word doorgewezen naar het hoofdmenu")
                return()

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
        os.system(clear)
        view ()
        print ()
        print ("Wat is de naam van het project dat je wilt verwijderen?")
        project_name = input()
        
        print ()
        print ("Wat is het project ID?")
        project_id = input()

        os.system("clear")
        headers = {'content-type': 'application/json'}
        url = "http://" + gns3_server + ":3080/v2/projects"
        r = requests.get(url, headers=headers)
        data = r.json()

        items = []
        for item in data:
            items.append(item['name'])

        if project_name in items:

            messagequestion(message_input= f"Weet je het zeker dat je het project {project_name} wilt verwijderen? (y/n)")
            conformation = input()

            if conformation == "y":

                items = []
                for item in data:
                    items.append(item['project_id'])

                if project_id in items:

                    url = f"http://{gns3_server}:3080/v2/projects/{project_id}"
                    requests.delete(url)
                    message (message_input="Het project is verwijderd")
                
                elif project_id not in items:
                    message(message_input="Project ID bestaat niet. Probeer het opnieuw")

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
        os.system (clear)
        view()
        print ()
        print ("Wat is de naam van het project dat je wilt exporteren?")
        project_name = input()
        print ()
        print ("Wat is het project ID?")
        project_id = input()
        print ()
        print ("Wat is de naam van het export bestand?")
        exportproject_name = input()

        os.system("clear")
        headers = {'content-type': 'application/json'}
        url = "http://" + gns3_server + ":3080/v2/projects"
        r = requests.get(url, headers=headers)
        data = r.json()

        items = []
        for item in data:
            items.append(item['name'])

        if project_name in items:
            items = []
            for item in data:
                items.append(item['project_id'])

            if project_id in items:

                cmd =f"{ssh} cat /mnt/project_templates/{exportproject_name}.gns3project"
                file_check = os.system(cmd)

                if file_check != "0":
                    messagequestion(message_input="Het bestand bestaat al wil je het bestand overschrijven? (y/n)")
                    conformation = input()

                    if conformation == "y":
                        print ()
                    
                    elif conformation == "n":
                        message("Taak is afgebroken door de gebruiker. Er zijn geen wijzigen doorgevoerd")
                        return()
                    
                    else:
                        message("Input niet herkend. Probeer het opnieuw")
            
            elif project_id not in item:
                message(message_input="Project ID bestaat niet. Probeer het opnieuw ")
                return()


            cmd = f"{ssh} curl http://{gns3_server}:3080/v2/projects/{project_id}/export -o /mnt/project_templates/{exportproject_name}.gns3project" 
            os.system (cmd)

            message (message_input="Het project is gexporteerd")
            

        else:
            message (message_input="Het project bestaat niet. Probeer het opnieuw")
        
        messagequestion (message_input="Wil je nog een project exporteren? (y/n)")
        conformation = input()
        
        if conformation == "y":
            print ()
        
        elif conformation == "n":
            print ()
            export = "off"

        else:
            message (message_input="Input niet herkend, je word doorgewezen naar het hoofdmenu")
            export = "off"
    
def imports ():
    imports = "on"
    while imports == "on":
        go = "on"
        os.system(clear)
        print()
        print("Wat is de naam van het nieuwe project?")
        project_name = input()

        os.system("clear")
        headers = {'content-type': 'application/json'}
        url = "http://" + gns3_server + ":3080/v2/projects"
        r = requests.get(url, headers=headers)
        data = r.json()

        items = []
        for item in data:
            items.append(item['name'])

        if project_name in items:
            message (message_input="Project bestaat al. Probeer het opnieuw")
            go = "off"
        
        if go == "on":
            cmd = ssh + "ls /mnt/project_templates/"
            command = os.system(cmd)
            print (command)
            print ()
            print ("Wat is de naam van de template dat je wilt importeren?")
            project_import = input()

            os.system(clear)
            print ("Nieuwe projectnaam: " + project_name)
            print ("Template: " + project_import)
            print ("")
            print ("Weet je het zeker dat je het project wilt importeren met de volgende gegevens? (y/n)")
            conformation = input ()

            if conformation == "y":
                
                id_first_part = str (random.randint(10000000, 99999999))
                project_id = f"{id_first_part}-0405-0607-0809-0a0b0c0d0e0f"

                cmd = f" 'cd /mnt/project_templates/ && curl -X POST -H Content-type: application/octet-stream --data-binary @{project_import}.gns3project http://{gns3_server}:3080/v2/projects/{project_id}/import?name={project_name}'"
                command = os.system (ssh + cmd)
                
                message (message_input="Het project is geimporteerd")
                imports = "off"

            elif conformation == "n":
                message (message_input="Er zijn geen wijzigingen aangebracht")
                imports = "off"

            else:
                message (message_input="input niet herkend. Probeer het opnieuw")
            
            messagequestion (message_input= "Wil je nog een project importeren? (y/n)")
            conformation = input()
            
            if conformation == "y":
                print ()
            
            elif conformation == "n":
                print ()
                imports = "off"
            else:
                message (message_input="Input niet herkend, je word doorgewezen naar het hoofdmenu")
                imports = "off"

def snapshot_view(project_id):
    os.system (clear)              
    #API request om snapshots te zien
    headers = {'content-type': 'application/json'}
    url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots"
    r = requests.get(url, headers=headers)
    data = r.json()

    if r.text == "[]":
        message (message_input="Er is zijn snapshots gemaakt voor dit project")
        return()
    
    else:
        df = pd.DataFrame.from_dict(data)
        print(df[['name', 'snapshot_id', 'created_at']])

def snapshot_create(project_id):
    message (message_input= "Wat is de naam van de snapshot?")
    answer = input()
    
    payload = {
        "name": answer,
    }

    #API request om de snapshot te maken 
    headers = {'content-type': 'application/json'}
    url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots"
    r = requests.post(url, json=payload, headers=headers)
    message (message_input = "De snapshot is gemaakt")

def snapshot_remove(project_id, project_name):
    os.system(clear)
    headers = {'content-type': 'application/json'}
    url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots"
    r = requests.get(url, headers=headers)
    data = r.json()
 
    snapshot_view(project_id)
    print()
    print("Wat is de naam van de snapshot dat je wilt verwijderen?")
    snapshot_name = input()

    items = []
    for item in data:
        items.append(item['name'])

    if snapshot_name not in items:
        message (message_input="Snapshot naam bestaat niet. Probeer het opnieuw")
        return()

    print ()
    print ("Wat is het ID van de snapshot?")
    snapshot_id = input()
    items = []
    for item in data:
        items.append(item['snapshot_id'])
    
    if snapshot_id not in items:
        message(message_input="Snapshot ID bestaat niet. Probeer het opniew")
        return()

    print ()
    messagequestion(message_input=f"Weet je het zeker dat je de snapshot {snapshot_name} met het ID {snapshot_id} wilt verwijderen (y/n)")
    conformation = input()

    if conformation == "y":
            headers = {'content-type': 'application/json'}
            url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots/{snapshot_id}"
            r = requests.delete(url, headers=headers)
            message (message_input="Snapshot is verwijderd")            
        
    elif conformation == "n":
        message(message_input="Taak afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd.")
    else:
        message(message_input="Input niet herkend probeer het opnieuw")

def snapshot_restore(project_id, project_name):
    snapshot_view(project_id)
    print ()
    print("Wat is het ID van de snapshot dat je wilt herstellen?")
    snapshot_id = input()

    messagequestion(f"Weet je het zeker dat je snapshot ID {snapshot_id} wilt herstellen? (y/n)")
    conformation = input ()

    if conformation == "y":
        headers = {'content-type': 'application/json'}
        url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots/{snapshot_id}/restore"
        r = requests.post(url, headers=headers)
        print (r.text)
        #time.sleep(10)
        message (message_input="Snapshot is hersteld")
        
    elif conformation == "n":
        message (message_input="Taak is afgebroken door de gebruiker")

    else:
        message (message_input="Input niet herkend. Er zijn geen wijzigingen uitgevoerd")

def snapshot_menu_check():
        go = "on"
        os.system(clear)
        view()
        print ()
        print ("Wat is de naam van het project?")
        project_name = input()

        print ()
        print ("Wat is het Project ID?")
        project_id = input()

        headers = {'content-type': 'application/json'}
        url = "http://" + gns3_server + ":3080/v2/projects"
        r = requests.get(url, headers=headers)
        data = r.json()

        items = []
        for item in data:
            items.append(item['name'])

        if project_name in items:

            items = []
            for item in data:
                items.append(item['project_id'])
            
            if project_id in items:

                #API request om het project te openen 
                headers = {'content-type': 'application/json'}
                url = "http://" + gns3_server + ":3080/v2/projects/" + project_id +"/open"
                r = requests.post(url, headers=headers)
                snapshot_menu(project_name, project_id)
            
            elif project_name not in items:
                os.system(clear)
                print ("Project bestaat niet. Probeer het opnieuw")
                time.sleep(sleepcounter)
                return()
            
        elif project_name not in items:
            os.system(clear)
            print ("Project bestaat niet. Probeer het opnieuw")
            time.sleep(sleepcounter)
            return()

def snapshot_menu (project_name, project_id):
    while start == "on":
        os.system(clear)
        print (title)
        print ()
        print_menu = f"Snapshots beheren van project {project_name} met project ID {project_id}"
        print (print_menu)
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
            input("Druk op enter om door te gaan...")


        elif answer == "2":
            snapshot_create(project_id)
        
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
    data = r.json()
    version_number = data['version']
    message(message_input= f"GNS3 versie: {version_number}")

def manage_projects():
    while start == "on":
        os.system(clear)
        print (title)
        print ("Beheer -> Templates beheren")
        print ()
        print ("1 - Templates weergeven")
        print ("2 - Template verwijderen")
        print ("3 - Terug gaan")
        print ("4 - Afsluiten")
        answer = input()

        if answer == "1":
            os.system(clear)
            cmd = ssh + "ls /mnt/project_templates/"
            command = os.system(cmd)
            print (command)
            input("Druk op enter om door te gaan...")

        elif answer == "2":
            messagequestion (message_input="Wat is de naam van de template die je wilt verwijderen?")
            answer = input()

            messagequestion (message_input=f"Weet je het zeker dat je {answer} wilt verwijderen? (y/n)")
            conformation = input()

            if conformation == "y":
                cmd = f"rm /mnt/project_templates/{answer}.gns3project"
                os.system(cmd)
                message ("Opdracht is uitgevoerd, check de lijst met projecten om te zien of het project nog bestaat")
                    
            elif conformation == "n":
                message(message_input="Taak afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd.")
            else:
                message(message_input="Input niet herkend probeer het opnieuw")

        elif answer == "3":
            return ()
            
        elif answer == "4":
            afsluiten()

def manage_nodes():
    os.system (clear)              
    #API request om snapshots te zien
    headers = {'content-type': 'application/json'}
    url = f"http://{gns3_server}:3080/v2/templates"
    r = requests.get(url, headers=headers)
    data = r.json()
    df = pd.DataFrame.from_dict(data)
    print(df[['name', 'template_id', 'template_type', 'category' ]])
    print ()
    input("Druk op enter om door te gaan...")

def manage_menu ():
    while start == "on":
        os.system(clear)
        print (title)
        print ("Beheer")
        print ()
        print ("1 - GNS3 versie weergeven")
        print ("2 - Templates beheren")
        print ("3 - Alle nodes bekijken")
        print ("4 - Terug gaan")
        print ("5 - Afsluiten")
        answer = input()

        if answer == "1":
            manage_checkversion()
        
        elif answer == "2":
            manage_projects()
        
        elif answer == "3":
            manage_nodes()

        elif answer == "4":
            return()
        
        elif answer == "5":
            afsluiten()
        
        elif answer != "1" or "2" or "3" or "4" or "5":
            message (message_input="Input niet herkend probeer het opnieuw")

def add_devices(project_id):
    counter_cloud = 0
    counter_fortigate = 0
    counter_switch = 0
    counter_pc = 0
    while start == "on":
        os.system(clear)

        print ("Apparaten toevoegen aan het nieuwe project")
        print ()
        print ("Optie   Apparaat               Aantal")
        print (f"1      Cloud gateways         {counter_cloud}")
        print (f"2      Fortigate firewalls    {counter_fortigate}")
        print (f"3      Cisco switches         {counter_switch}")       
        print (f"4      Virtuele PC's          {counter_pc}")
        print ("")
        print ("5 - Apparaten toevoegen")
        print ()
        print ("Welke optie wil je gebruiken?")
        answer = input()

        if answer == "1":
            device_name = "Cloud gateways"
        
        elif answer == "2":
            device_name = "Fortigate firewalls"

        elif answer == "3":
            device_name = "Cisco switches"

        elif answer == "4":
            device_name = "Virtuele PC's"

        elif answer == "5":
            
            if counter_cloud != 0:
                coordinate_x = 200
                coordinate_y = 0
                for x in range(counter_cloud):
                    r=requests.post(f"http://{gns3_server}:3080/v2/projects/{project_id}/templates/{template_cloud}", json={"x":coordinate_x, "y":coordinate_y})
                    coordinate_x += 200
            
            if counter_fortigate != 0:
                coordinate_x = 200
                coordinate_y = 100
                for x in range(counter_fortigate):
                    requests.post(f"http://{gns3_server}:3080/v2/projects/{project_id}/templates/{template_fortigate}", json={"x":coordinate_x, "y":coordinate_y})
                    coordinate_x += 100
                
            if counter_switch != 0:
                coordinate_x = 200
                coordinate_y = 200
                for x in range(counter_fortigate):
                    requests.post(f"http://{gns3_server}:3080/v2/projects/{project_id}/templates/{template_switch}", json={"x":coordinate_x, "y":coordinate_y})
                    coordinate_x += 100
            
            if counter_pc != 0:
                coordinate_x = 200
                coordinate_y = 300
                for x in range(counter_pc):
                    r = requests.post(f"http://{gns3_server}:3080/v2/projects/{project_id}/templates/{template_pc}", json={"x":coordinate_x, "y":coordinate_y})
                    print (r.text)
                    coordinate_x += 100
            
            message(message_input="De apparaten zijn toegevoegd.")
            return()
        else:
            message(message_input="Input niet herkend. Probeer het opniew")        

        messagequestion(f"Hoeveel {device_name} wil je toevegen?")
        answer = input()

        if device_name == "Cloud gateways":
            counter_cloud = int(answer)
        
        elif device_name == "Fortigate firewalls":
            counter_fortigate = int(answer)
        
        elif device_name == "Cisco switches":
            counter_switch = int(answer)
        
        elif device_name == "Virtuele PC's":
            counter_pc = int(answer)

def afsluiten():
        os.system (clear)
        print ("Bye, Bye")
        time.sleep (sleepcounter)
        os.system("rm ~/.session")
        exit()

while start == "on":       
    os.system (clear)
    print ("GNS3 Management Tool")
    print ()
    print ("1 - Lijst met projecten weergeven")
    print ("2 - Project aanmaken")
    print ("3 - Apparaten toevoegen aan een project")
    print ("4 - Project verwijderen")
    print ("5 - Project exporteren")
    print ("6 - Project importeren")
    print ("7 - Snapshot")
    print ("8 - Beheer")
    print ()
    print ("9 - Afsluiten")
    print ("10 - Naar shell gaan")
    print ()
    print ("Vul het nummer van de optie die je wilt gebruiken.")
    answer = input ()

    if answer == "1":
        view ()
        print ()
        input("Druk op enter om door te gaan...")

    elif answer == "2":
        create () 

    elif answer == "3":
        os.system(clear)
        view ()
        print ()
        print ("Wat is het project ID waaraan je de apparaten wilt toevoegen?")
        project_id = input()
        add_devices(project_id)

    elif answer == "4":
        remove ()

    elif answer == "5":
        export ()

    elif answer == "6":
        imports ()
    
    elif answer == "7":
        snapshot_menu_check ()
    
    elif answer == "8":
        manage_menu ()

    elif answer == "9":
        afsluiten()

    elif answer != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        message (message_input="Input niet herkend probeer het opnieuw")