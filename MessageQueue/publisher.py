#!/usr/bin/env python
import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ['RABBITMQ_HOST']))
channel = connection.channel()

payload = {'humidity': 80, 'temperature': 30.1,
    	   'carbon_monoxide': 20, 'optical_dust': 30}  # mock payload data 

channel.queue_declare(queue='air_quality_data')

channel.basic_publish(exchange='',
                      routing_key='air_quality_data',
                      body=payload)
connection.close()
