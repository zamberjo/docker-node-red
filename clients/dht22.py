# -*- coding: utf-8 -*-
# Jose Zambudio Bernabeu <zamberjo@gmail.com>

# pip install paho-mqtt
import paho.mqtt.client as mqtt
# $: git clone https://github.com/adafruit/Adafruit_Python_DHT
# $: python setup.py install
import Adafruit_DHT
import logging

_logger = logging.getLogger(__name__)
logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
fileHandler = logging.FileHandler("dht22.log")
fileHandler.setFormatter(logFormatter)
_logger.addHandler(fileHandler)

broker_address="192.168.0.19"
sensor = Adafruit_DHT.DHT22
pin = 4

client = mqtt.Client("P1")
client.connect(broker_address)

client.loop_start()

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
client.publish("/house/office/temperature", "%.2f" % (temperature))
client.publish("/house/office/humidity", "%.2f" % (humidity))
_logger.info("Humedad %r | Temperatura %r" % (humidity, temperature))

client.loop_stop()
