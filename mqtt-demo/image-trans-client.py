import paho.mqtt.publish as publish
import base64
import paho.mqtt.client as mqtt

host = "127.0.0.1"
port = 1883
user = "admin"
pwd = "123456"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    print(msg.topic + " sent")

with open("./mqtt-demo/test.jpg",'rb') as f:
    res = base64.b64encode(f.read())
byteArr = bytearray(res)

client = mqtt.Client()
client.username_pw_set(user, pwd)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port, 600)
client.publish('image', payload=byteArr, qos=1)
