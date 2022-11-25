import configparser
from inspect import Parameter
import random
from tracemalloc import Snapshot
import requests
import re
import argparse
import platform
import os
import os.path
import time
import json
import pandas as pd
from pathlib import Path

# Alle mogelijke parameters. De optie parameter "optie" is verplicht bij het gebruik
parser = argparse.ArgumentParser(description = "GNS3 Management Tool")
parser.add_argument("-o", "--optie", help = "Optie", required = False, default = "")
parser.add_argument("-s", "--show", help = "Laat dingen zien", required = False, default = "")
parser.add_argument("-pn", "--projectnaam", help = "Project aam", required = False, default = "")
parser.add_argument("-pid", "--projectid", help = "Project ID", required = False, default = "")
parser.add_argument("-exn", "--exportnaam", help = "Export naam", required = False, default = "")
parser.add_argument("-imn", "--importnaam", help = "Import naam", required = False, default = "")
parser.add_argument("-sn", "--snapshotnaam", help = "Snapshot naam", required = False, default = "")
parser.add_argument("-sid", "--snapshotid", help = "Snapshot ID", required = False, default = "")
parser.add_argument("-tn", "--templatenaam", help = "Template naam", required = False, default = "")
parser.add_argument("-ram", "--ram", help = "GNS3 RAM", required = False, default = "")
parser.add_argument("-cpu", "--cpu", help = "GNS3 CPU's", required = False, default = "")
parser.add_argument("-core", "--core", help = "GNS3 Core's", required = False, default = "")
parser.add_argument("-b", "--bevesteging", help = "Bevestegeging", required = False, default = "")

argument = parser.parse_args()
status = False

if argument.optie:
    status = True

# Config inlezen
config = configparser.ConfigParser()
config.read('config.ini')
gns3_server = config['default']['gns3_server']
ssh_username = config['default']['ssh_username']

template_cloud = config['templates']['cloud']
template_fortigate = config['templates']['fortigate']
template_switch = config['templates']['switch']
template_pc = config['templates']['pc']

vmware_host = config['vmware']['host']
vmware_username = config['vmware']['username']
vmware_password = config['vmware']['password']
vmware_vm_name = config['vmware']['vm_name']

# Standaard variabelen die gebruikt worden 
sleepcounter = 2
option = ""
start = "on"
title = "GNS3 Management Tool"
ssh = ("ssh " + ssh_username + "@" + gns3_server + " ")
clear = ("clear")

# Functie voor het het uitprinten van een bericht op een nette manier
def message (message_input):
    os.system(clear)
    print (message_input)
    time.sleep(2)

# Functie voor het het uitprinten van een vraag op een nette manier
def messagequestion (message_input):
    os.system(clear)
    print (message_input)

# Functie met daarin alle mogelijkheden om data op te halen en weer te geven.
def view (option):
    # Laat de bestaande GNS3 zien
    if option == "projects":
        os.system(clear)
        headers = {'content-type': 'application/json'}
        url = f"http://{gns3_server}:3080/v2/projects"
        r = requests.get(url, headers=headers)
        data = r.json()

        df = pd.DataFrame.from_dict(data)
        print(df[['name', 'project_id']])
    
    # Laat alle projecten zien die geimporteerd kunnen worden
    if option == "templates":
        os.system(clear)
        cmd = ssh + "ls /mnt/project_templates/"
        command = os.system(cmd)
        print (command)

    # Laat alle applainces die op de server staan zien
    if option == "nodes":
        os.system (clear)              
        headers = {'content-type': 'application/json'}
        url = f"http://{gns3_server}:3080/v2/templates"
        r = requests.get(url, headers=headers)
        data = r.json()
        df = pd.DataFrame.from_dict(data)
        print(df[['name', 'template_id', 'template_type', 'category' ]])
        print ()   

# Functie om projecten aan te maken
def create (project_name, conformation, exit_after_finish):
    go = "on"
    if project_name == "":
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

    # Als de projectnaam bestaat word het script afgebroken
    if project_name in items:
        message (message_input="Project bestaat al. Probeer het opnieuw")
        time.sleep (sleepcounter)
        go = "off"

    if go == "on":

        if conformation == "":
            messagequestion (message_input="Weet je het zeker dat je een nieuw project wilt starten met de naam " + project_name + "? (y/n)")
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

            if exit_after_finish == True:
                exit()

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

# Functie om projecten te verwijderen
def remove (project_name, project_id, conformation, exit_after_finish):
    remove = "on"
    while remove == "on": 
        os.system(clear)
        if project_name == "" or project_id== "":
            view (option="projects")
            print ()
            print ("Wat is de naam van het project dat je wilt verwijderen?")
            project_name = input()
            
            print ()
            print ("Wat is het project ID?")
            project_id = input()

        # Haalt de huidige lijst met projecten op en vergelijkt dit met de input
        os.system("clear")
        headers = {'content-type': 'application/json'}
        url = "http://" + gns3_server + ":3080/v2/projects"
        r = requests.get(url, headers=headers)
        data = r.json()

        items = []
        for item in data:
            items.append(item['name'])

        if project_name in items:
            if conformation == "":
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
            
            if exit_after_finish == True:
                exit()

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

# Functie om projecten te importeren    
def export (project_name, project_id, export_name, exit_after_finish):
    export = "on"
    while export == "on":
        os.system (clear)
        if project_name == "":
            view(option="projects")
            print ()
            print ("Wat is de naam van het project dat je wilt exporteren?")
            project_name = input()
        
        if project_id == "":
            print ()
            print ("Wat is het project ID?")
            project_id = input()
        
        if export_name == "":
            print ()
            print ("Wat is de naam van het export bestand?")
            export_name = input()

        # Haalt de huidige lijst met projecten op en vergelijkt het met de input
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
                
                # Chect of er al een export bestaat met de naam van de input
                check_export = os.path.isfile(f"/mnt/project_templates/{export_name}.gns3project")

                if check_export == False:
                    print (check_export)
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


            cmd = f"{ssh} curl http://{gns3_server}:3080/v2/projects/{project_id}/export -o /mnt/project_templates/{export_name}.gns3project" 
            os.system (cmd)

            message (message_input="Het project is gexporteerd")
            

        else:
            message (message_input="Het project bestaat niet. Probeer het opnieuw")
        
        if exit_after_finish == True:
            exit()

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

# Functie om projecten te importeren    
def imports (project_name, import_name, conformation, exit_after_finish):
    imports = "on"
    while imports == "on":
        go = True

        if project_name == "":
            os.system(clear)
            print()
            print("Wat is de naam van het nieuwe project?")
            project_name = input()

        # Controleert of de naam van het nieuwe project bestaat
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
            go = False
        
        if go == True:
            if import_name == "":
                cmd = ssh + "ls /mnt/project_templates/"
                command = os.system(cmd)
                print (command)
                print ()
                print ("Wat is de naam van de template dat je wilt importeren?")
                import_name = input()
            
            if conformation == "":
                os.system(clear)
                print ("Nieuwe projectnaam: " + project_name)
                print ("Template: " + import_name)
                print ("")
                print ("Weet je het zeker dat je het project wilt importeren met de volgende gegevens? (y/n)")
                conformation = input ()

            # Het project importeren met shell commando's
            if conformation == "y":
                
                id_first_part = str (random.randint(10000000, 99999999))
                project_id = f"{id_first_part}-0405-0607-0809-0a0b0c0d0e0f"

                cmd = f" 'cd /mnt/project_templates/ && curl -X POST -H Content-type: application/octet-stream --data-binary @{import_name}.gns3project http://{gns3_server}:3080/v2/projects/{project_id}/import?name={project_name}'"
                command = os.system (ssh + cmd)
                
                message (message_input="Het project is geimporteerd")
                imports = "off"

            elif conformation == "n":
                message (message_input="Er zijn geen wijzigingen aangebracht")
                imports = "off"

            else:
                message (message_input="input niet herkend. Probeer het opnieuw")

            if exit_after_finish == True:
                exit()
            
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

# Functie dat een lijst genereerd van de beschikbare snapshots van het project
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

# Functie om een snapshot te maken
def snapshot_create(project_id, snap_name):
    if snap_name == "":
        message (message_input= "Wat is de naam van de snapshot?")
        snap_name = input()
    
    payload = {
        "name": snap_name,
    }

    #API request om de snapshot te maken 
    headers = {'content-type': 'application/json'}
    url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots"
    r = requests.post(url, json=payload, headers=headers)
    message (message_input = "De snapshot is gemaakt")

# Functie om een snapshot te verwijderen
def snapshot_remove(project_id, snap_name, snap_id, conformation):
    os.system(clear)
    headers = {'content-type': 'application/json'}
    url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots"
    r = requests.get(url, headers=headers)
    data = r.json()

    if snap_name == "":
        snapshot_view(project_id)
        print()
        print("Wat is de naam van de snapshot dat je wilt verwijderen?")
        snap_name = input()

    items = []
    for item in data:
        items.append(item['name'])

    if snap_name not in items:
        message (message_input="Snapshot naam bestaat niet. Probeer het opnieuw")
        return()

    if snap_id == "":
        print ()
        print ("Wat is het ID van de snapshot?")
        snap_id = input()

    items = []
    for item in data:
        items.append(item['snapshot_id'])
    
    if snap_id not in items:
        message(message_input="Snapshot ID bestaat niet. Probeer het opniew")
        return()

    if conformation == "":
        print ()
        messagequestion(message_input=f"Weet je het zeker dat je de snapshot {snap_name} met het ID {snap_id} wilt verwijderen (y/n)")
        conformation = input()

    if conformation == "y":
            headers = {'content-type': 'application/json'}
            url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots/{snap_id}"
            r = requests.delete(url, headers=headers)
            message (message_input="Snapshot is verwijderd")            
        
    elif conformation == "n":
        message(message_input="Taak afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd.")
    else:
        message(message_input="Input niet herkend probeer het opnieuw")

# Functie om snapshots te herstellen
def snapshot_restore(project_id, snap_id, conformation):
    if snap_id == "":
        snapshot_view(project_id)
        print ()
        print("Wat is het ID van de snapshot dat je wilt herstellen?")
        snap_id = input()

    if conformation == "":
        messagequestion(f"Weet je het zeker dat je snapshot ID {snap_id} wilt herstellen? (y/n)")
        conformation = input ()

    if conformation == "y":
        headers = {'content-type': 'application/json'}
        url = f"http://{gns3_server}:3080/v2/projects/{project_id}/snapshots/{snap_id}/restore"
        requests.post(url, headers=headers)
        message (message_input="Snapshot is hersteld")
        
    elif conformation == "n":
        message (message_input="Taak is afgebroken door de gebruiker")

    else:
        message (message_input="Input niet herkend. Er zijn geen wijzigingen uitgevoerd")

def snapshot_menu_check():
        go = "on"
        os.system(clear)
        view(option="projects")
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

# Het menu dat uitgeprint word bij het beheren van snapshots
def snapshot_menu (project_name, project_id):
    while start == "on":
        snap_name = ""
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
            snapshot_create(project_id, snap_name)
        
        elif answer == "3":
            snapshot_remove(project_id, snap_name, snap_id, conformation)                

        elif answer == "4":
            snapshot_restore(project_id, snap_id, conformation)
        
        elif answer == "5":
            snapshot_menu_check()
        
        elif answer == "6":
            return ()
        
        elif answer == "7":
            afsluiten()
        
        elif answer != "1" or "2" or "3" or "4" or "5" or "6" or "7":
            os.system (clear)
            print ("Input niet herkend probeer het opnieuw")
            time.sleep (sleepcounter)

# Functie dat het versie nummer van GNS3 op vraagt
def manage_checkversion():
    os.system(clear)
    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_server + ":3080/v2/version"
    r = requests.get(url, headers=headers)
    data = r.json()
    version_number = data['version']
    print (f"GNS3 versie: {version_number}")

# Functie om een template te verwijderen
def manage_projects_remove(template_name, conformation):
    if template_name == "":
        messagequestion (message_input="Wat is de naam van de template die je wilt verwijderen?")
        template_name = input()

    if conformation == "":
        messagequestion (message_input=f"Weet je het zeker dat je {template_name} wilt verwijderen? (y/n)")
        conformation = input()

    if conformation == "y":
        cmd = f"rm /mnt/project_templates/{template_name}.gns3project"
        os.system(cmd)
        message ("Opdracht is uitgevoerd, check de lijst met projecten om te zien of het project nog bestaat")
            
    elif conformation == "n":
        message(message_input="Taak afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd.")
    else:
        message(message_input="Input niet herkend probeer het opnieuw")

# Menu dat uitgeprint word voor het beheren van de GNS3 installatie
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
            view(option="templates")
            input("Druk op enter om door te gaan...")

        elif answer == "2":
            manage_projects_remove(template_name="", conformation="")
            
        elif answer == "3":
            return ()
            
        elif answer == "4":
            afsluiten()

# Functie voor het aanpassen van de systeem recources van de GNS3 VM
def manage_server(gns3_ram ="", gns3_cpu="", gns3_cores="", conformation = ""):
    if gns3_ram == "":
        messagequestion(message_input="Hoeveel RAM wil je aan de GNS3 server geven?")
        gns3_ram = input()

    if gns3_cpu == "":
        messagequestion(message_input="Hoeveel CPU's wil je aan de GNS3 server geven? ")
        gns3_cpu = input()

    if gns3_cores == "":
        messagequestion(message_input="Hoeveel CPU cores wil je aan de GNS3 server geven?")
        gns3_cores = input()

    # Print een overzicht uit met de ingevulde waardes
    if conformation =="":
        os.system(clear)
        print ("Overzicht - GNS3 VM upgraden/downgraden")
        print ()
        print (f"RAM:                {gns3_ram}")
        print (f"CPU's:              {gns3_cpu}")
        print (f"Cores per CPU:      {gns3_cores}")
        print ()
        print ("Kloppen deze gegevens? (y/n)")
        conformation = input ()

    # Powershell commando's die uitgevoerd moeten worden.
    if conformation == "y":
        cmd1 = "Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false" + "\n"
        cmd2 = f"Connect-VIServer -Server {vmware_host} -Protocol https -User {vmware_username} -Password {vmware_password}" + "\n"
        cmd3 = f"Stop-VM -VM {vmware_vm_name} -confirm:$false" + "\n"
        cmd4 = f"Get-VM -Name {vmware_vm_name} | Set-VM -MemoryGB {gns3_ram} -NumCpu {gns3_cpu} -CoresPerSocket {gns3_cores} -confirm:$false" + "\n"
        cmd5 = f"Start-VM -VM {vmware_vm_name} -confirm:$false" + "\n"

        # Bovenstaande regels weg schrijven naar een bestand
        a_file = open("./vmware-gns3.ps1", "r")
        list_of_lines = a_file.readlines()
        
        list_of_lines[0] = cmd1
        list_of_lines[1] = cmd2
        list_of_lines[2] = cmd3
        list_of_lines[3] = cmd4
        list_of_lines[4] = cmd5

        a_file = open("./vmware-gns3.ps1", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        
        # Het Powershell script uitvoeren
        message (message_input="Het script word zo uitgevoerd.")
        os.system("pwsh ./vmware-gns3.ps1")
        message("De GNS3 server is geupgraded. Het kan nog een paar minuten totdat de server weer bereikbaar is.")
    
    elif conformation == "n":
        message(message_input="Taak is afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd")
    
    else:
        message(message_input="Input niet herkend. Probeer het opniew")

# Het menu dat utigeprint word bij de optie beheer
def manage_menu ():
    while start == "on":
        os.system(clear)
        print (title)
        print ("Beheer")
        print ()
        print ("1 - GNS3 versie weergeven")
        print ("2 - Templates beheren")
        print ("3 - Alle nodes bekijken")
        print ("4 - Server hardware aanpassen")
        print ("5 - Terug gaan")
        print ("6 - Afsluiten")
        answer = input()

        if answer == "1":
            manage_checkversion()
            time.sleep(2)
        
        elif answer == "2":
            manage_projects()
        
        elif answer == "3":
            view(option="nodes")
            input("Druk op enter om door te gaan...")
        
        elif answer == "4":
            manage_server(gns3_ram ="", gns3_cpu="", gns3_cores="", conformation = "")

        elif answer == "5":
            manage_server()
            return()
        
        elif answer == "6":
            afsluiten()
        
        elif answer != "1" or "2" or "3" or "4" or "5" or "6":
            message (message_input="Input niet herkend probeer het opnieuw")

# Functie om systeem recources van de GNS3 VM aan te passen
def add_devices(project_id):
    # Standaard waardes
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
            # Van elke optie word er een loop uitgevoerd als de waarde boven de 0 is. Verder er bij elke applaince een ander coordinaat gegenereerd anders overlappen ze elkaar in GNS3
            
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

# Functie dat gebruikt word bij het afsluiten van het script
def afsluiten():
        os.system (clear)
        print ("Bye, Bye")
        time.sleep (sleepcounter)
        exit()

# Als er argumenten zijn gegeven, dan word deze functie gebruikt om te checken welke functionaliteit er uitgevoerd moet worden. Daarbij worden ook 
# de variabelen die nodig zijn mee gestuurd
def arguments(option, project_name, project_id, export_name, import_name, snap_name, snap_id, show, template_name, gns3_ram, gns3_cpu, gns3_core, conformation):
    exit_after_finish = True

    if option == "view":
        view(option="projects")
    
    elif option == "project_create":
        create (project_name,conformation, exit_after_finish)
    
    elif option == "project_remove":
        remove (project_name, project_id, conformation, exit_after_finish)
    
    elif option == "project_export":
        export(project_name, project_id, export_name, exit_after_finish)
    
    elif option == "project_import":
        imports(project_name, import_name, conformation, exit_after_finish)
    
    elif option == "snap_view":
        snapshot_view(project_id)
    
    elif option == "snap_create":
        snapshot_create(project_id, snap_name)
    
    elif option == "snap_remove":
        snapshot_remove(project_id, snap_name, snap_id, conformation)
    
    elif option == "snap_restore":
        snapshot_restore(project_id, snap_id, conformation)

    elif option == "show":
        view (show)
    
    elif option == "template_remove":
        manage_projects_remove (template_name, conformation)
    
    elif option == "upgrade_vm":
        manage_server (gns3_ram, gns3_cpu, gns3_core, conformation)
        
    else:
        message(message_input="Optie bestaat niet. Probeer het opnieuw")
    
    exit()

# Start staat altijd aan om een constante loop van het script te behouden
while start == "on":
    # Als er argumenten zijn gebruikt dan worden die hieronder in variableen gezet en naar de functie arguments word gestuurd 
    if status == True:
        option = argument.optie
        conformation = argument.bevesteging
        project_name = argument.projectnaam
        project_id = argument.projectid
        export_name = argument.exportnaam
        import_name = argument.importnaam
        snap_name = argument.snapshotnaam
        snap_id = argument.snapshotid
        show = argument.show
        template_name = argument.templatenaam
        gns3_ram = argument.ram
        gns3_cpu = argument.cpu
        gns3_core = argument.core
        arguments(option, project_name, project_id, export_name, import_name, snap_name, snap_id, show, template_name, gns3_ram, gns3_cpu, gns3_core, conformation)
    
    # Het hoofdmenu
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
    print ()
    print ("Vul het nummer van de optie die je wilt gebruiken.")
    answer = input ()

    if answer == "1":
        view (option="projects")
        print ()
        input("Druk op enter om door te gaan...")

    elif answer == "2":
        create (project_name="", conformation="", exit_after_finish=False) 

    elif answer == "3":
        os.system(clear)
        view (option="projects")
        print ()
        print ("Wat is het project ID waaraan je de apparaten wilt toevoegen?")
        project_id = input()
        add_devices(project_id)

    elif answer == "4":
        remove (project_name="", project_id="", conformation="", exit_after_finish=False)

    elif answer == "5":
        export (project_name="", project_id="", export_name="", exit_after_finish=False)

    elif answer == "6":
        imports (project_name="", import_name="", conformation="", exit_after_finish=False)
    
    elif answer == "7":
        snapshot_menu_check ()
    
    elif answer == "8":
        manage_menu ()

    elif answer == "9":
        afsluiten()

    elif answer != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        message (message_input="Input niet herkend probeer het opnieuw")
