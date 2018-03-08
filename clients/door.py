# -*- coding: utf-8 -*-
# Jose Zambudio Bernabeu <zamberjo@gmail.com>

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

print "*/5 * * * * source /opt/pruebas/venv/bin/activate  && python /opt/pruebas/dht22.py >/dev/null 2>&1"

broker_address="192.168.0.19"

GPIO.setmode(GPIO.BOARD)
DOOR_SENSOR_PIN = 12

# def on_message(client, userdata, message):
#     print("message received " ,str(message.payload.decode("utf-8")))
#     print("message topic=",message.topic)
#     print("message qos=",message.qos)
#     print("message retain flag=",message.retain)
# client.on_message=on_message

GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
client = mqtt.Client("P1")
# client.username_pw_set("USER", password="PASSWOºRD")
client.connect(broker_address)
# client.subscribe("house/door")

client.loop_start()

isOpen = oldIsOpen = None
while True:
    oldIsOpen = isOpen
    isOpen = GPIO.input(DOOR_SENSOR_PIN)
    if (isOpen and (isOpen != oldIsOpen)):
        client.publish("/house/door", "OPEN")
    elif (isOpen != oldIsOpen):
        client.publish("/house/door", "CLOSED")
    time.sleep(0.1)


# print("Publishing message to topic", "house/door")
# client.publish("/house/door", "OPEN")

# time.sleep(4)

client.loop_stop()
