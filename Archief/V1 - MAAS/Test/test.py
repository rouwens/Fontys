import sys
import os
import requests

system = sys.platform

if system == 'win32':
    username = os.getlogin()
    download_path = "'C:\\Users\\" + username + "\Downloads'"


elif system == 'linux':
    download_path = "~/Downloads"

import random
num1 = random.randint(000000000, 999999999)
print (num1)