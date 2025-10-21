from config import channel

message = "hello, this is my first message"

channel.basic_publish(exchange="", routing_key="letterbox", body=message)

print("sent message : {}".format(message))

channel.close()
