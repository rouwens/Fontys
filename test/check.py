import os
import subprocess
username = os.getlogin()
x = os.path.isfile("/Users/" + username + "/.ssh/id_rsa")
print (x)
print (username)