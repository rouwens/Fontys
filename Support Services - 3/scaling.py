import os
import time
import random
import string
from random import randrange


start = 1
monitor = "aan"
naam_genereren = "uit"
vm_uitrollen = "uit"

arry = ["leeg", "leeg", "leeg"]
counter = 0

timer = 2
# Percentage van het CPU gebruik    
percentage_voor_actie = "70.0"

# Aantal seconde dat de load boven de ingestelde waarde moet zitten
load_time_up = 5

# Aantal seconde dat de load onder de ingestelde waarde moet zitten
load_time_down = 20


while start == 1:
    while monitor == "aan":

        # Download cpu gebruik bestand
        os.system("touch cpu_docker.txt & wget 192.168.123.30:8080 -O cpu_docker.txt >/dev/null 2>&1")
        
        # Bestand openen
        cpu_info_web_bestand = open("cpu_docker.txt", "r+")
        cpu_info_web_lezen = cpu_info_web_bestand.read()
        # Bestand sluiten
        cpu_info_web_bestand.close()

        #Output omzetten naar een string
        cpu_info_web = str (cpu_info_web_lezen)
        #print (cpu_info_docker)

        os.system("rm cpu_docker.txt")

        if cpu_info_web > percentage_voor_actie:
            print (cpu_info_web)
            print ("Hoog CPU gebruik")
            time.sleep(load_time_up)

            if cpu_info_web > percentage_voor_actie:
                print (cpu_info_web)
                print ("Nog steeds hoog CPU gebruik. VM word nu uitgerold")
                monitor = "uit"

                if counter != 3:
                    counter += 1
                    str_counter = str(counter)
                    vm_naam = "scaling-webserver-" + str_counter
                    vm_uitrollen = "aan"
                
                else:
                    print ("Maximum VM's ingezet")
                    time.sleep(1)
            
        else:
            print ("Laag CPU gebruik")
            time.sleep(2)

    while vm_uitrollen == "aan":
        cmd1 = 'Get-VM Webserver-test| Get-HardDisk | Copy-HardDisk -DestinationPath "[Servers] ' + vm_naam + '/HDD" -DestinationStorageFormat Thin' + "\n"
        cmd2 = 'New-VM -Name ' + vm_naam + ' -Datastore Servers -NumCPU 1 -MemoryGB 2 -NetworkName "Host-only" -Floppy -CD  -GuestID debian10_64Guest -DiskPath "[Servers] ' + vm_naam + '/HDD.vmdk"' + "\n"
        cmd3 = 'Start-VM -VM "'+ vm_naam + '"' + "\n"

        a_file = open("vm_kopieren.ps1", "r")
        list_of_lines = a_file.readlines()

        list_of_lines[2] = cmd1
        list_of_lines[3] = cmd2
        list_of_lines[4] = cmd3

        a_file = open("vm_kopieren.ps1", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

        cmd = "scp vm_kopieren.ps1 daan@100.105.92.26:/home/daan"
        os.system (cmd)

        cmd = "ssh daan@100.105.92.26 'pwsh /home/daan/vm_kopieren.ps1'"
        os.system (cmd)

        monitor = "aan"
        vm_uitrollen = "uit"