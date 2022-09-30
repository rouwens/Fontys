import os
import requests
import time
from tabulate import tabulate
import json
import ast
import pandas as pd


gns3_server = "192.168.253.2"

def message (message_input):
    os.system("clear")
    print (message_input)
    time.sleep(2)

os.system("clear")
headers = {'content-type': 'application/json'}
url = "http://" + gns3_server + ":3080/v2/projects"
r = requests.get(url, headers=headers)
data = r.json()

json_data = json.dumps(data)
item_dict = json.loads(json_data)
print (len(item_dict))

#TABEL PRINTEN
#df = pd.DataFrame.from_dict(data)
#print(df[['name', 'project_id']])


items = []
for item in data:
    items.append(item['name'])

#print (data['project_id'])
#print (data)

#version_number = data['version']
#message(message_input= f"Versie: {version_number}")