from random import randrange
import time
import string
import random

arry = ["leeg", "leeg", "leeg"]

vm_naam_1 = "leeg"
vm_naam_2 = "leeg"
vm_naam_3 = "leeg"

getal =randrange(3)

naam_genereren = "aan"

while naam_genereren == "aan":
    foo = [1, 2, 3]
    getal = random.choice(foo)
    getal_str = str(getal)
    naam = "vm_naam_" + getal_str
    print (naam)
    
    if naam == "leeg":
        lengte = 5
        letters = string.ascii_lowercase
        willekeurige_string = ''.join(random.choice(letters) for i in range(lengte))
        vm_naam = "webserver-" + willekeurige_string
        naam = vm_naam
        print (naam)
        time.sleep(1)

    else:
        print ("Deze plek is bezet")
        time.sleep(1)
    