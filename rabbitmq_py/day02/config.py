import pika

credentials = pika.PlainCredentials("jexhsu", "wsdfr")

connection_parameters = pika.ConnectionParameters("localhost", credentials=credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare("hello")
