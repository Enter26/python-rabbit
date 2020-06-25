try:
    import env
    import psycopg2
    import pika
    import json

except Exception as e:
	print("Exception - {}".format_map(e))

credentials = pika.PlainCredentials(username=env.user, password=env.password)
parameters=pika.ConnectionParameters(env.queue_host, env.queue_port, env.queue_name, credentials)
connection = pika.BlockingConnection(parameters)
print("conected")

channel = connection.channel()
channel.queue_declare(queue=env.queue_channel)


def callback(ch, method, properties, body):
    
    print(" [x] Received %r" % body)
    
    #query = "INSERT INTO data () VALUES()"
    #conn = psycopg2.connect(host=env.db_host, port=env.db_port, database=env.db_name,
    #        user=env.db_user, password=env.db_password)
    #cur = conn.cursor()

    #cur.commit()

    #con.close()
channel.basic_consume(queue=env.queue_name, on_message_callback=callback, auto_ack=True)
    
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
