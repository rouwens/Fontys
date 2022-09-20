import configparser
import random
import requests
import mysql.connector as mysql
import re
import paramiko
import sys
import os

#config bestand inladen en algemene variabelen toewijzen
config = configparser.ConfigParser()
config.read('config.ini')
gns3_server = config['default']['gns3_server']

#DB config inladen
db = mysql.connect(
    host = config['database']['host'],
    user = config['database']['user'],
    passwd = config['database']['pwd'],
    database = config['database']['database'],
    )
cursor = db.cursor()

project_name = "test"

getprojectid = """SELECT project_id FROM `projects` WHERE `name` = %s"""
cursor.execute(getprojectid, (project_name, ))
fetch = cursor.fetchall()
clean = str(fetch)
#project_id = re.sub(r'[^\w\s]', '', clean)


project_id = clean[3:-4]
#project_id = project_id[:13] + "-" + project_id[0:]
print (project_id)

cursor.close()
db.close()