import paho.mqtt.client as mqtt 
import time

#callback for message event
def on_message(client, userdata, message):
  print("message received " ,str(message.payload.decode("utf-8")))
  print("message topic=",message.topic)
  print("message qos=",message.qos)
  print("message retain flag=",message.retain)

broker_address="iot.eclipse.org"
print("creating new instance")
#create new instance
client = mqtt.Client("1")
#attach function to callback
client.on_message=on_message
print("connecting to broker")
client.connect(broker_address) 
client.loop_start() 
client.subscribe("house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")
time.sleep(1)
client.loop_stop() 