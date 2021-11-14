import psutil
import os

start = 1

while start == 1:
    cpu = psutil.cpu_percent(0.5)
    cpu_str = str(cpu)
    cmd = "echo " + cpu_str + " > index.html"
    os.system(cmd)