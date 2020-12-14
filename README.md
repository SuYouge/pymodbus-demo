# python-demos for modbus client

![ScreenShot](./pyqt5-demo/ScreenShot.png)

## virtual env guide

[virtual env guide](https://www.cnblogs.com/freely/p/8022923.html)

13:00 - 21:00

## pyqt5-demo

### We need

* show some static text
* serial comm panel
* led indicator for io signal
* plot line for analog signal

```
pyuic5 -o serial_panel.py serial_panel.ui
```

## mqtt-demo

### Mosquitto

#### install
1. [install guide](https://mosquitto.org/blog/2013/01/mosquitto-debian-repository/)
2. and run `sudo apt install mosquitto-clients`
3. [config user group](https://www.cnblogs.com/yangyangming/p/12628209.html)
4. [config item list](https://www.cnblogs.com/chen1-kerr/p/7258487.html)
5. [set id and passwd](https://www.cnblogs.com/zkwarrior/p/10950294.html)

#### test
run instruction under 3 terminal
```bash
mosquitto -c /etc/mosquitto/mosquitto.conf -v # run service
mosquitto_sub -v -t richie -p 1883 # run server
mosquitto_pub -t richie -m hello -p 1883 # run client
```

#### simple-demo

[paho-mqtt-API](https://www.cnblogs.com/lnn123/p/10837754.html)

[mqtt-simple-server](./mqtt-demo/mqtt-simple-server.py)
[mqtt-simple-client](./mqtt-demo/mqtt-simple-client.py)

#### image-transport

[mqtt-image-transport](https://gist.github.com/WakeupTsai/6cac70f8e9f26cc909e9223346580a0f)