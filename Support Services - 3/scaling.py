import os
import time
import random
import string

start = 1

timer = 2
# Percentage van het CPU gebruik    
percentage_voor_actie = "70.0"

# Aantal seconde dat de load boven de ingestelde waarde moet zitten
load_time_up = 5

# Aantal seconde dat de load onder de ingestelde waarde moet zitten
load_time_down = 20

def vm_uitrollen():
<<<<<<< Updated upstream
    lengte = 5
    letters = string.ascii_lowercase
    willekeurige_string = ''.join(random.choice(letters) for i in range(lengte))
    vm_naam = "webserver-" + willekeurige_string
    cmd = "xe vm-copy vm=webserver sr-uuid=3fb6bb78-b43f-6db0-5734-6f710733500f new-name-label=" + vm_naam
=======
    print ("VM uigerold")
>>>>>>> Stashed changes

while start == 1:

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
            print ("Nog steeds hoog CPU gebruik")
<<<<<<< Updated upstream
            vm_uitrollen()
=======
            vm_uitrollen()            
>>>>>>> Stashed changes
        
    
    else:
        print ("Laag CPU gebruik")
        time.sleep(2)