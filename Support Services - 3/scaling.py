import os
import time

# Standaard waarden van de while loops 
start = 1
monitor = "aan"
vm_uitrollen = "uit"
vm_verwijderen = "uit"

counter = 0

timer = 2
# Percentage van het CPU gebruik    
percentage_voor_actie = 70

# Aantal seconde dat de load boven de ingestelde waarde moet zitten
load_time_up = 5

# Aantal seconde dat de load onder de ingestelde waarde moet zitten
load_time_down = 5

# Maximum aantal VM's dat erbij mogen komen 
max_vm_counter = 3

while start == 1:
    while monitor == "aan":

        cmd = "ssh 192.168.123.11 'cpu_info'"
        result = os.popen(cmd)
        cpu_info_web = int(result.read())


        if cpu_info_web > percentage_voor_actie:
            print (cpu_info_web)
            print ("Hoog CPU gebruik")
            time.sleep(load_time_up)

            cmd = "ssh 192.168.123.11 'cpu_info'"
            result = os.popen(cmd)
            cpu_info_web = int(result.read())

            if cpu_info_web > percentage_voor_actie:
                print (cpu_info_web)
                print ("Nog steeds hoog CPU gebruik. VM word nu uitgerold")
                monitor = "uit"

                if counter != max_vm_counter:
                    counter += 1
                    str_counter = str(counter)
                    vm_naam = "scaling-webserver-" + str_counter
                    vm_uitrollen = "aan"
                
                else:
                    print ("Maximum VM's ingezet")
                    monitor = "aan"
                    time.sleep(1)


        if cpu_info_web < percentage_voor_actie:
            print ("Laag CPU gebruik")
            time.sleep(load_time_down)

            cmd = "ssh 192.168.123.11 'cpu_info'"
            result = os.popen(cmd)
            cpu_info_web = int(result.read())

            if cpu_info_web < percentage_voor_actie:
                if counter != 0:
                    print ("VM verwijderen")
                    time.sleep (1)
                    str_counter = str(counter)
                    vm_naam = "scaling-webserver-" + str_counter
                    counter -= 1
                    monitor = "uit"
                    vm_verwijderen = "aan"

                
                else:
                    print ("Er zijn geen VM's om te verwijderen")
                    time.sleep(1)
            
            else:
                print ("CPU gebruik is nog steeds te hoog.")

    while vm_uitrollen == "aan":
        cmd1 = 'Get-VM webserver-scaling-default| Get-HardDisk | Copy-HardDisk -DestinationPath "[Servers] ' + vm_naam + '/HDD" -DestinationStorageFormat Thin' + "\n"
        cmd2 = 'New-VM -Name ' + vm_naam + ' -Datastore Servers -NumCPU 1 -MemoryGB 2 -NetworkName "Host-only" -Floppy -CD  -GuestID debian10_64Guest -DiskPath "[Servers] ' + vm_naam + '/HDD.vmdk"' + "\n"
        cmd3 = 'Start-VM -VM "'+ vm_naam + '"' + "\n"

        a_file = open("vm_uitrollen.ps1", "r")
        list_of_lines = a_file.readlines()

        list_of_lines[2] = cmd1
        list_of_lines[3] = cmd2
        list_of_lines[4] = cmd3

        a_file = open("vm_uitrollen.ps1", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

        cmd = "scp vm_uitrollen.ps1 daan@100.105.92.26:/home/daan"
        os.system (cmd)

        cmd = "ssh daan@100.105.92.26 'pwsh /home/daan/vm_uitrollen.ps1'"
        os.system (cmd)

        monitor = "aan"
        vm_uitrollen = "uit"

    while vm_verwijderen == "aan":
        cmd1 = "Stop-VM -VM " + vm_naam + " -Confirm:$false" + "\n"
        cmd2 = "Remove-VM -VM " + vm_naam + " -Confirm:$false" + "\n"
        
        a_file = open("vm_verwijderen.ps1", "r")
        list_of_lines = a_file.readlines()

        list_of_lines[2] = cmd1
        list_of_lines[3] = cmd2

        a_file = open("vm_verwijderen.ps1", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

        cmd = "scp vm_verwijderen.ps1 daan@100.105.92.26:/home/daan"
        os.system (cmd)

        cmd = "ssh daan@100.105.92.26 'pwsh /home/daan/vm_verwijderen.ps1'"
        os.system (cmd)

        monitor = "aan"
        vm_verwijderen = "uit"
