import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4  # This pin refers to the GPIO pin that you have connected the DHT22 outpin pin to in your pi!

def get_dht22_value():
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else: 
        return 0, 0
