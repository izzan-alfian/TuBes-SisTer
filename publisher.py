import paho.mqtt.client as mqtt
import time
import datetime

broker_address="localhost"
print("creating new instance")
client = mqtt.Client("P1")
print("connecting to broker")
client.connect(broker_address, port=3333)


client.loop_start()

print("Publishing message to topic","airport/announcement")
client.publish("airport/announcement", "Perubahan jadwal/lokasi, silahkan cek airport/location dan airport/time")

print("Publishing message to topic","airport/location")
client.publish("airport/location", "Boarding G12")

print("Publishing message to topic","airport/time")
now = datetime.datetime.now()
client.publish("airport/time", str(now))

time.sleep(1)
client.loop_stop()