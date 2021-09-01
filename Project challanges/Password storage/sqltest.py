import random
import time
#from mysql.connector.errors import custom_error_exception
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
cursor = db.cursor()

salt = "Gekke"
userid = "16"

cursor.execute("UPDATE accounts SET salt = %s WHERE id = %s;", (salt, userid))
db.commit()