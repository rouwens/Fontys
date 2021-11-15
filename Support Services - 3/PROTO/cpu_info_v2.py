import socket
import psutil
import mysql.connector as mysql
import time

start = 1 #Zo laten staan anders werkt de tool niet
timer = 2 #Tijd in senconde

# Database connectie
db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "scaling_s3",
    )
cursor = db.cursor()

while start == 1:
    # CPU gebruik ophalen
    cpu = psutil.cpu_percent(0.5)
    cpu_str = str(cpu)

    # IP adres ophalen
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = (s.getsockname()[0])
    s.close()

    # Gegevens versturen
    get_sql = """UPDATE `cpu_info` SET `cpu_percentage` = %s WHERE `cpu_info`.`ip` = %s; ;"""
    cursor.execute(get_sql, (cpu, ip,))
    time.sleep(timer)