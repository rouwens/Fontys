from random import randrange
import time


arry = ["leeg", "leeg", "daan"]
getal =randrange(3)

keuze = arry[getal]
if keuze != "leeg":
    print (getal)
    print ("Keuze is niet leeg")

else:
    print (getal)
    print ("Keuze is leeg")


