import os
import time

# Standaard waarden van de while loops 
start = 1
monitor = "aan"
opgeschaald = 0

timer = 2
# Percentage van het CPU gebruik    
percentage_voor_actie = 70

# Aantal seconde dat de load boven de ingestelde waarde moet zitten
load_time_up = 5

# Aantal seconde dat de load onder de ingestelde waarde moet zitten
load_time_down = 5


while start == 1:
    while monitor == "aan":

        cmd = "ssh 100.68.60.88 'cpu_info'"
        result = os.popen(cmd)
        cpu_info_web = int(result.read())


        if cpu_info_web > percentage_voor_actie:
            print (cpu_info_web)
            print ("Hoog CPU gebruik")
            time.sleep(load_time_up)

            cmd = "ssh 100.68.60.88 'cpu_info'"
            result = os.popen(cmd)
            cpu_info_web = int(result.read())

            if cpu_info_web > percentage_voor_actie:
                print ("Nog steeds hoog CPU gebruik. Webserver word opgeschaald")
                
                if opgeschaald != 1:
                    cmd = "pwsh vm_opschalen.ps1"
                    opgeschaald = 1
                    os.system (cmd)
                    time.sleep(20)
                
                else:
                    print ("De VM is al opgeschaald.")
                    time.sleep(1)


        if cpu_info_web < percentage_voor_actie:
            print ("Laag CPU gebruik")
            time.sleep(load_time_down)

            cmd = "ssh 100.68.60.88 'cpu_info'"
            result = os.popen(cmd)
            cpu_info_web = int(result.read())

            if cpu_info_web < percentage_voor_actie:

                if opgeschaald != 0:
                   cmd = "pwsh vm_afschalen.ps1"
                   opgeschaald = 0
                   os.system(cmd)
                   time.sleep(20)
                
                else:
                    print ("De VM is al afgeschaald")