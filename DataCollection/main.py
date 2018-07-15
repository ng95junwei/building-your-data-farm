from dht22 import get_dht22_value
from mq7 import get_mq7_value
from gp2y10 import get_gp2y10_value

while True:

    humidity, temperature = get_dht22_value()
    carbon_monoxide = get_mq7_value()
    optical_dust = get_gp2y10_value()

    payload = {'humidity': humidity, 'temperature': temperature,
    		   'carbon_monoxide': carbon_monoxide, 'optical_dust': optical_dust}
    # Send the request to our message queue
