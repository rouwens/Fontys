import os
import time

def func_ping():
    timer = 5
    ping = os.system("ping -c 1 google.com")
    date = os.system("date >> ping.log")

    if ping == 0:
        with open("ping.log", "a") as ping_log:
            ping_log.write("Host is bereikbaar")
            date
            ping_log.write("\n")
            ping_log.write("\n")

    else:
        with open("ping.log", "a") as ping_log:
            ping_log.write("Host is niet bereikbaar")
            date
            ping_log.write("\n")
            ping_log.write("\n")

    time.sleep (timer)
    func_ping()

func_ping()
