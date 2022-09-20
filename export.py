import json
import requests
import configparser
import os
import sys
import random
import paramiko
import time
import socket

#config bestand inladen en algemene variabelen toewijzen
config = configparser.ConfigParser()
config.read('config.ini')
gns3_server = config['default']['gns3_server']

#SSH client
ssh = paramiko.SSHClient()
ssh_username = config['default']['ssh_username'] 
ssh_location_private_key = config['default']['ssh_location_private_key']

