import random
import string

lengte = 5
letters = string.ascii_lowercase
willekeurige_string = ''.join(random.choice(letters) for i in range(lengte))
vm_naam = "webserver-" + willekeurige_string
cmd = "xe vm-copy vm=webserver sr-uuid=3fb6bb78-b43f-6db0-5734-6f710733500f new-name-label=" + vm_naam

print (cmd)