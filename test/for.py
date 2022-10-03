import requests
import configparser
import os
import time

clear = "clear"
start = "on"
project_id = "54099455-0405-0607-0809-0a0b0c0d0e0f" 

config = configparser.ConfigParser()
config.read('config.ini')
gns3_server = config['default']['gns3_server']
ssh_username = config['default']['ssh_username']

template_cloud = config['templates']['cloud']
template_fortigate = config['templates']['fortigate']
template_switch = config['templates']['switch']
template_pc = config['templates']['pc']

def message (message_input):
    os.system(clear)
    print (message_input)
    time.sleep(2)

def messagequestion (message_input):
    os.system(clear)
    print (message_input)


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
                #coordinate_x = int(coordinate_x)
                coordinate_x += 50
                #coordinate_x = str(coordinate_x)

        
        if counter_fortigate != 0:
            coordinate_x = 300
            coordinate_y = 0
            for x in range(counter_fortigate):
                cmd = f"http://{gns3_server}:3080/v2/projects/{project_id}/templates/{template_fortigate}"
                r = requests.post(cmd, json={"x":coordinate_x, "y":coordinate_y}) 
                print (cmd)
                print (r.text)
                coordinate_x += 50
        
        #message(message_input="De apparaten zijn toegevoegd.")
        exit()
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