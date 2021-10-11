import os
import time

os.system("clear")
def start():

    print ("Wat is de software die je wilt installeren?")
    software = input()
    print ()

    if software == "vlc":
        print ()

    else:
        print ()
        print ("Deze software is niet ondersteund")
        time.sleep(2)
        os.system("clear")
        start()

    print ("Wat is het IP adres van de machine?")
    ip = input()
    print ()

    cmd = "sshpass -p daan0409 ssh -o StrictHostKeyChecking=no localadmin@" + ip + " 'echo daan0409 | sudo -S apt install " + software + " -y '"
    os.system(cmd)

    exit (0)

start ()
