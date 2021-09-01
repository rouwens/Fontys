import paho.mqtt.client as mqtt
import time

def start ():
    def funcmqqt (setkleur):
        kleur = setkleur
        client = mqtt.Client()
        client.connect("192.168.178.200",1883,60)
        client.publish("rouwens/stoplicht", kleur);
        client.disconnect();
        start()
    
    print ()
    print ("Type hier je kleur in. (rood,geel,groen) of uit")
    print ("Vul stop in om het programma te stoppen")
    kleur = input()

    if kleur == "rood":
        setkleur = "rood"
        funcmqqt (setkleur)

    elif kleur == "geel":
        setkleur = "geel"
        funcmqqt (setkleur)
    
    elif kleur == "groen":
        setkleur = "groen"
        funcmqqt (setkleur)
    
    elif kleur == "uit":
        setkleur = "uit"
        funcmqqt (setkleur)

    elif kleur == "stop":
        exit ()

    else:
        print ("Kleur niet herkend...")
        time.sleep(2)
        start()

start()