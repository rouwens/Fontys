import configparser
import random
from tracemalloc import Snapshot
import requests
import mysql.connector as mysql
import re
import argparse
import platform
import os
import os.path
import time
import paramiko
import json
from pathlib import Path


cmd = "C:\Windows\System32\OpenSSH\ssh.exe ub_localadmin@192.168.253.2  ls /mnt"
command = os.system(cmd)
print (command)
print (cmd)
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls /mnt")
#print(ssh_stdout.read().decode())
input("Druk op enter om door te gaan...")