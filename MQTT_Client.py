from paho.mqtt.client import Client, MQTTMessage, MQTTv5
from time import sleep
# from MQTTInterface import Comm_Interface
class MQTT_Client():
    def __init__(self, host, username, password, port=1883):
        self._client = Client(protocol=MQTTv5)
        self._client.username_pw_set(username, password)
        self._client.on_message = self._on_message
        self._client.on_connect = self._on_connect
        self._client.on_connect_fail = self._on_connect_fail
        self._msg = []
        self._callback = None
        # self._client.on_subscribe = self._subscribe
        self._host = host
        self._port = port
        self._userdata = None
        self.connect()
    def connect(self):
        self._client.connect(self._host, port=self._port)
        self._client.loop_start()
        sleep(0.1)
    def disconnect(self):
        self._client.loop_stop(force = True)
        self._client.disconnect()
        print("connection disconnected")
    def setOnMessagecallback(self,callback):
        self._callback = callback

    def _on_message(self, client, userdata, message: MQTTMessage):
        msgPayload = []
        topic = message.topic
        msgr = str(message.payload.decode("utf-8"))
        msgPayload.append(topic)
        msgPayload.append(msgr)
        if self._callback is not None:
            self._callback(msgPayload)
 
    def message(self):
        msglist = self._msg
        return msglist
    def _on_connect(self, client, data, flags, reason, properties=0):
        print("Connected")
        # client : Client
        # print(f"Sub: {client.subscribe('#')}")
    def _subscribe(self,topic):
        return self._client.subscribe(topic)
        
    def _publish(self,topic,msg):
        return self._client.publish(topic,msg)

    def testMsg(self):
        self._testMsg = '123'
        return self._testMsg
    def _on_connect_fail(self, client, userdata):
        print("Connection failed", client, userdata)
    
    def _on_disconnect(self, client, userdata):
        # self._client.loop_stop(force = True)
        self._client.on_disconnect = self._on_disconnect
        # print("connection disconnected")
    def __str__(self):
        return "This is a the MQTT class"


# mqttTopics = {
# "System/Sensor/Temperature/Value":0,
# "System/Sensor/Humidity/Value":0,
# "System/Sensor/Temperature/Error":0,
# "System/Sensor/Humidity/Error":0,
# "System/Cooler/inCommand":0,
# "System/Cooler/outCommand":0,
# "System/Cooler/Serial":0
# }
# mqttTopics = [
# "Sensor/Temperature/Value",
# "Sensor/Humidity/Value",
#  ]
# mqtt = MQTT_Client("192.168.1.161", "okori", "jude")
# mqtt.connect()
# while(1):

#     sleep(0.5)
#     mqtt._subscribe(mqttTopics[0])
#     sleep(2)
#     mqtt._publish(mqttTopics[0],"10")
#     print("Sent")
#     sleep(0.25)
#     print(mqtt.message())
#     mqtt.disconnect()
#     mqtt._client.loop_stop()
