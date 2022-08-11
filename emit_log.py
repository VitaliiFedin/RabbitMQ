import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:0]) or 'Hello World!'
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f'[x] Sent {message}')
connection.close()
