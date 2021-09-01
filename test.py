import random
import time
import requests
import string
import mysql.connector as mysql
import re
import hashlib
import base64
import platform
import os

db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "passwordmanager"
    )
cursor = db.cursor()

cmd = "echo 3 | ping -c 1 rouwens.ddns.net >/dev/null 2>&1"

check = os.system(cmd)
print(check)