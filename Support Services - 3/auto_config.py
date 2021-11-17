import socket
import re
import mysql.connector as mysql
import os

# Database connectie
db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "scaling_s3",
    )
cursor = db.cursor()

# IP ophalen van de machine en interpuncties eruit halen.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_heel = (s.getsockname()[0])
s.close()
ip = re.sub(r'[^\w\s]', '', ip_heel)

# De gewenste hostname ophalen en doorvoeren
get_sql = """SELECT hostname FROM `scaling` WHERE `ip` = %s ;"""
cursor.execute(get_sql, (ip,))
sql_hostname = cursor.fetchall()

pre_hostname = str(sql_hostname)
hostname = pre_hostname[3:-4]

cmd = "hostnamectl set-hostname " + hostname
os.system(cmd)