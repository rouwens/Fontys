import os
import time

start = 1

timer = 2
# Percentage van het CPU gebruik    
percentage_voor_actie = "70.0"

# Aantal seconde dat de load boven de ingestelde waarde moet zitten
load_time_up = 10

# Aantal seconde dat de load onder de ingestelde waarde moet zitten
load_time_down = 20

while start == 1:

    # Download cpu gebruik bestand
    os.system("touch cpu_docker.txt & wget 192.168.123.30:8080 -O cpu_docker.txt >/dev/null 2>&1")
    
    # Bestand openen
    cpu_info_docker_bestand = open("cpu_docker.txt", "r+")
    cpu_info_docker_lezen = cpu_info_docker_bestand.read()
    # Bestand sluiten
    cpu_info_docker_bestand.close()

    #Output omzetten naar een string
    cpu_info_docker = str (cpu_info_docker_lezen)
    #print (cpu_info_docker)

    os.system("rm cpu_docker.txt")

    if cpu_info_docker > percentage_voor_actie:
        print ("Hoog CPU gebruik")
        time.sleep(load_time_up)