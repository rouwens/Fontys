import base64

str_example = "Python is the best programming language"
str_to_bytes = str_example.encode("ascii") #we have an encoded string
bytes_to_base64= base64.b64encode(str_to_bytes)#encoding bytes to base64
print(bytes_to_base64)
#returns decoded string of base64
base64_output = bytes_to_base64.decode('ascii')
print(base64_output)

import random
import time
import requests
import string
import mysql.connector as mysql
import re
import hashlib
import base64

db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "passwordmanager"
    )
#cursor = db.cursor()
#username = "drouwens"
#switch = """SELECT `key` FROM `accounts` WHERE `accounts`.`username` = %s;"""
#cursor.execute(switch, (username,))

#sql = cursor.fetchall()
#strsql = str(sql)
#key = strsql[3:-4]
#print (key)

test = "ZGFhbjA0MDk="
b64_str = test
b64_str = b64_str.encode('ascii')
b64_bytes = base64.b64decode(b64_str)
decode_str = b64_bytes.decode('ascii')
print(decode_str)



