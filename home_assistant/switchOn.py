import paho.mqtt.client as paho
import sys  # Library imports

def switchOn():
    client = paho.Client()  # Signals a connection to paho MQTT client

    if client.connect("99.99.124.212", 1883,
                      60) != 0:  # Attempts to connect to MQTT broker on raspberry pi, ip = 172.17.0.1, port = 1883, keepalive=60, (!=0 signifies if the connection fails)
        print("Could not connect to MQTT Broker!")  # Error message for if the connection fails
        sys.exit(-1)  # Exits

    client.publish("homeassistant/lights")  # Publishes the MQTT packet "homeassistant/lights"
    client.disconnect()  # Disconnects the client

