import os
import sys
import re
cliinput = (str(sys.argv))

# IP adres uit de string filteren
temphost = cliinput[30:]
split_host = temphost.split("'", 1)
host = split_host[0]

#De naam van de software eruit filteren
tempsoftware = split_host[1]
cuttempsoftware = tempsoftware[3:]
split_software = cuttempsoftware.split("'", 1)
str_split_software = str(split_software)
software = re.sub(r'[^\w\s]', '', str_split_software)

if software == "vlc":
    print ("vlc install")

cmd = "sshpass -p daan0409 ssh -o StrictHostKeyChecking=no localadmin@" + host + " 'echo daan0409 | sudo -S apt install " + software + " -y'"
os.system (cmd)
