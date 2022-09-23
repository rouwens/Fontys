import maas.client

client = maas.client.connect("http://192.168.219.51:5240/MAAS/", apikey="rz56FLCCq7Z2vG2pAg:mDCyXNTgsf2QDxmA6C:hZ5xXD46EpLstVAR7Bd6XWUNAB3Lu9ks")

test = client.machines.list()

print (test)
#for machine in client.machines.list():
    #print(repr(machine))

    #print (machine)

#from oauthlib.oauth1 import SIGNATURE_PLAINTEXT # fades
#from requests_oauthlib import OAuth1Session # fades

#MAAS_HOST = "http://192.168.219.51:5240/MAAS"
#CONSUMER_KEY, CONSUMER_TOKEN, SECRET = "rz56FLCCq7Z2vG2pAg:mDCyXNTgsf2QDxmA6C:hZ5xXD46EpLstVAR7Bd6XWUNAB3Lu9ks".split(":")

#maas = OAuth1Session(CONSUMER_KEY, resource_owner_key=CONSUMER_TOKEN, resource_owner_secret=SECRET, signature_method=SIGNATURE_PLAINTEXT)

#nodes = maas.get(f"{MAAS_HOST}/api/2.0/machines/", params={"op": "commission"})
#nodes = maas.get(f"{MAAS_HOST}/api/2.0/machines/")

#nodes.raise_for_status()

#print(nodes.json())