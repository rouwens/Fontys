import time

begin = 1
start = 1
twee = 2

while begin == 1:
    while start == 1:
        print ("1")
        time.sleep(1)
        print ("2")
        time.sleep(1)
        start = 0
        twee = 3

    while twee == 3:
        print ("In de loop")
        twee = 2
        start = 1
        time.sleep(1)