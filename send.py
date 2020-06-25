#import
import env
try:
    import random
    import pika
    import os, glob

except Exception as e:
    print("Exception -{}".format_map(e))

#create random number 
body = random.randint(0,40)
print(body)


#connection to queue
credentials = pika.PlainCredentials(username=env.user, password=env.password)
parameters=pika.ConnectionParameters(env.queue_host, env.queue_port, env.queue_name, credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=env.queue_channel)

#send data to queue
channel.basic_publish(exchange='',routing_key=env.routing_key, body=str(body))
print(" [x] Sent ",body)

#close connection
connection.close()

