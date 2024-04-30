import paho.mqtt.client as paho
import sys
import time

def onMessage(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode())

client = paho.Client()
client.on_message = onMessage

if client.connect("172.17.0.1", 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

# Add a loop to allow the client to process incoming messages
client.loop_start()

# Publish a message to the topic "homeassistant/lights" with payload "Hello, MQTT!"
client.publish("homeassistant/lights", "Hello, MQTT!")

# Wait for a short time to allow the message to be processed
time.sleep(2)

# Disconnect from the broker
client.disconnect()