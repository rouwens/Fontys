import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  client.subscribe("rouwens/stoplicht")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "rood":
    print("Het stoplicht staat op rood")

  if msg.payload.decode() == "geel":
    print("Het stoplicht staat op geel")
  
  if msg.payload.decode() == "groen":
      print("Het stoplicht staat op groen")

  if msg.payload.decode() == "uit":
      print ("Het stoplicht staat uit")
   
    
client = mqtt.Client()
client.connect("192.168.178.200",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()