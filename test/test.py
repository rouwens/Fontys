import json
import os
import requests
import time
from tabulate import tabulate
import json
import ast
import pandas as pd


gns3_server = "192.168.253.2"

os.system("clear")
headers = {'content-type': 'application/json'}
url = "http://" + gns3_server + ":3080/v2/projects"
r = requests.get(url, headers=headers)
data = r.json()

json_data = json.dumps(data)
item_dict = json.loads(json_data)
project_counter = int((len(item_dict)))

items = []
for item in data:
    items.append(item['name'])

project_id = data['project_id']
firstserver = item_dict
print (firstserver)