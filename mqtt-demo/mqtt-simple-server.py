import paho.mqtt.client as mqtt

host = "127.0.0.1"
port = 1883
user = "admin"
pwd = "123456"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.username_pw_set(user, pwd)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port, 600)
client.subscribe('fifa', qos=0)
client.loop_forever()