import platform
import os

sys = platform.system()

if sys == "Windows":
    print ()

elif sys == "Linux" or "Darwin":
    if sys == "Linux":
        ssh_private_key = os.path.isfile("~/.ssh/id_rsa")
    
    elif sys == "Darwin":
        username = os.getlogin()
        ssh_private_key = os.path.isfile("/Users/" + username + "/.ssh/id_rsa")

    if ssh_private_key == True:
        print ("SSH sleutel bestaat")