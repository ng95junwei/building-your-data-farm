#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ['RABBITMQ_HOST']))
channel = connection.channel()

channel.queue_declare(queue='air_quality_data')

def callback(ch, method, properties, body):
	print("Consume!!")  # We will define this in the next part!

channel.basic_consume(callback,
                      queue='air_quality_data',
                      no_ack=True)

channel.start_consuming()
