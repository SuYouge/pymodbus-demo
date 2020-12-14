import paho.mqtt.client as mqtt
import base64

host = "127.0.0.1"
port = 1883
user = "admin"
pwd = "123456"

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("image")
  
def on_message(client, userdata, msg):
    img = base64.b64decode(msg.payload)
    file = open('./mqtt-demo/sdjflksd.jpg','wb')
    file.write(img)
    file.close()
    print ('image received')
  
client = mqtt.Client()
client.username_pw_set(user, pwd)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port, 600)
client.loop_forever()