import os
import subprocess
import time

def func_ping(url):


    timer = 5
    ping = os.system("ping -c 1 {0}".format(url))
    date = os.system("date >> ping.log")

    if ping == 0:
        with open("ping.log", "a") as ping_log:
            ping_log.write(url + " is bereikbaar")
            date
            ping_log.write("\n")
            ping_log.write("\n")

    else:
        with open("ping.log", "a") as ping_log:
            ping_log.write( url + " is niet bereikbaar")
            date
            ping_log.write("\n")
            ping_log.write("\n")

    time.sleep (timer)
    func_ping(url)


print ("Vul hier de URL in van de website die je wilt checken op de beschikbaarheid")
url = input()
func_ping(url)


