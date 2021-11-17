import os
import time

start = 1

while start == 1:
    waarde = 70
    cmd = "ssh 192.168.123.30 'cpu_info'"
    result = os.popen(cmd)
    cpu_info_web = int (result.read())

    if cpu_info_web > waarde:
        print ("Meer dan wat is ingesteld. VM opschalen")

    if cpu_info_web < waarde:
        print ("Onder de waarde dat is ingesteld")
    
    time.sleep(1)