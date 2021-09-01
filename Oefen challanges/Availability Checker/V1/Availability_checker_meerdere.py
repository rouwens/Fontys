import os
import time

def func_ping():
    timer = 5
    host_google = os.system("ping -c 1 google.com")
    host_facebook = os.system("ping -c 1 facebook.com")
    host_linkedin = os.system("ping -c 1 linkedin.com")
    date = os.system("date >> ping-meerdere.log")

    if host_google == 0:
        with open("ping-meerdere.log", "a") as ping_log:
            ping_log.write("Google is bereikbaar")
            date
            ping_log.write("\n")

    else:
        with open("ping-meerdere.log", "a") as ping_log:
            ping_log.write("Google is niet bereikbaar")
            date
            ping_log.write("\n")

    if host_facebook == 0:
        with open("ping-meerdere.log", "a") as ping_log:
            ping_log.write("Facebook is bereikbaar")
            ping_log.write("\n")

    else:
        with open("ping-meerdere.log", "a") as ping_log:
            ping_log.write("Facebook is niet bereikbaar")
            ping_log.write("\n")

    if host_linkedin == 0:
        with open("ping-meerdere.log", "a") as ping_log:
            ping_log.write("Lnkedin is bereikbaar")
            ping_log.write("\n")
            ping_log.write("\n")

    else:
        with open("ping-meerdere.log", "a") as ping_log:
            ping_log.write("linkedin is niet bereikbaar")
            ping_log.write("\n")
            ping_log.write("\n")

    time.sleep (timer)
    func_ping()

func_ping()
