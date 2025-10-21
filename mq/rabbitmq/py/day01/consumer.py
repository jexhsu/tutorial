from config import channel


def on_message_received(ch, method, properties, body):
    print("received new message : {}".format(body))

channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback=on_message_received)

print("Starting Consuming") 

channel.start_consuming()
