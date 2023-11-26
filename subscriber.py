import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received: " , str(message.payload.decode("utf-8")))

    if message.topic == "airport/time":
        with open("boarding.txt", "w") as timeFile:
            timeFile.write(str(message.payload.decode("utf-8")))

    if message.topic == "airport/location":
        with open("location.txt", "w") as locationFile:
            locationFile.write(str(message.payload.decode("utf-8")))


print("Creating client")
client = mqtt.Client("P2")
client.on_message = on_message
print("Conecting to broker")
client.connect("localhost", port = 3333)

client.loop_start()
print("Subscribing")
client.subscribe("airport/announcement")
client.subscribe("airport/location")
client.subscribe("airport/time")

time.sleep(60)
client.loop_stop()