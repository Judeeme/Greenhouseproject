from MQTT_Client import MQTT_Client
import json
import random
from time import sleep, time
from datetime import datetime
from sensors import sensors
from database import db

class backend(sensors,db):
    def __init__(self):
        sensors.__init__(self)
        db.__init__(self)
        # db.createtable(self)
        # self.sensor = sensors()
        self.Temperature = "Temperature"
        self.Humidity = "Humidity"
        self.soil = "Soil"
        self.CO2 = "CO2"
        self.light = "Light"
        self.ke = {self.Temperature:0,self.Humidity:0,self.soil:0,self.CO2:0,self.light:0}
        self.Client = MQTT_Client
        # MQTT_Client.setOnMessagecallback(self._on_message)
        self.Client = MQTT_Client("192.168.0.101", "raspi-home", "123456")
        self.Topic = "Plant/Sensor"
    def readSensors(self):
        sensorsVal = sensors.readSensors(self)
        self.Data = dict(zip(self.ke, sensorsVal))
        # print(self.Data)
    def databaseWrite(self):
        dbaseVal = self.Data
        dbaseVal["Time"] = (float(f'{time():0.2f}'))
        db.setValues(self,dbaseVal)  
    def publishData(self):
        jdata = json.dumps(self.Data,sort_keys=True,indent=3)
        self.Client._publish(self.Topic,jdata)
    def simulatesensor(self):
        self.readSensors()
        self.publishData()
        self.databaseWrite()
# Client = MQTT_Client("192.168.0.101", "raspi-home", "123456")
TestBackend = backend()
# TestBackend.readSensors()
while(1):
    TestBackend.simulatesensor()
    print(datetime.now())
    # print(float(f'{time():0.2f}'))
    sleep(5)

    