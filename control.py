from MQTT_Client import MQTT_Client
import json
import random
from sensors import sensors
from time import sleep, time
from datetime import datetime
from dataLogger import dataLogger
# class dataLogger():
#     def __init__(self):
#         self.filename = f'log{datetime.now()}.log'
#         self.file = open(self.filename, "a")
#         self.file.write("Time\t Temperature\t Humidity\t CO2\t light\t soil_Moisture\n")
#     def logData(self,sensorData: dict):
#         self.file.write(f'{int(time())}\t {sensorData["Temperature"]}\t {sensorData["Humidity"]}\t {sensorData["CO2"]}\t {sensorData["light"]}\t {sensorData["soil_Moisture"]}\n')
        

class backend(dataLogger):
    def __init__(self):
        self.sensors = sensors()
        self.dataLogger = dataLogger()
        # self.sensor = sensors
        self.Client = MQTT_Client
        # MQTT_Client.setOnMessagecallback(self._on_message)
        self.Client = MQTT_Client("192.168.1.161", "raspi-home", "123456")
        self.Topic = "Plant/Sensor"
    def readallsensors(self):
        self.Temperature = "Temperature"
        self.Humidity = "Humidity"
        self.co2 = "CO2"
        self.light = "light"
        self.soilmoistures = "soil_Moisture"
        self.Data = dict()
        dataTemp = self.sensors.readSensors()
        self.Data[self.Temperature] = dataTemp[0]
        self.Data[self.Humidity] = dataTemp[1]
        self.Data[self.soilmoistures] = dataTemp[2]
        self.Data[self.co2] = dataTemp[3]
        self.Data[self.light] = dataTemp[4]
        return self.Data
    def publishData(self):
        jdata = json.dumps(self.Data,sort_keys=True,indent=3)
        self.Client._publish(self.Topic,jdata)
    def simulatecontrol(self):
        self.readallsensors()
        self.publishData()
        self.dataLogger.logData(self.Data)
# Client = MQTT_Client("192.168.0.101", "raspi-home", "123456")
TestBackend = backend()
while(1):
    TestBackend.simulatecontrol()
#     print(TestBackend.Data)
    print(time(), TestBackend.Data)
    sleep(60)
# controlOBJ = backend()
# print(controlOBJ.readallsensors())










# class sensors():
#     ''' 
#     This class is responsible for 
#     reading the sensor data from the 
#     raspberry pi
#     '''
#     def __init__(self):
#         print("sensor called")
#         self.Temperature = "Temperature"
#         self.Humidity = "Humidity"
#         self.co2 = "CO2"
#         self.light = "light"
#         self.soilmoistures = "soil_Moisture"
#         self.Data = dict()
#     def readTemp(self,temperature):
#         self.Data[self.Temperature] = temperature
#     def readHum(self,humidity):
#         self.Data[self.Humidity] = humidity
#     def readCO2(self,co2):
#         self.Data[self.co2] = co2
#     def readSoilMositure(self,soilmoisture):
#         self.Data[self.soilmoistures] = soilmoisture
#     def readlight(self,light):
#         self.Data[self.light] = light
#     def simulatesensor(self):
#         randTemp = random.randint(0,100)
#         randHum = random.randint(0,100)
#         randCO2 = random.randint(0,100)
#         randlight = random.randint(0,100)
#         randSoilMoisture = random.randint(0,100)
#         self.readTemp(randTemp)
#         self.readHum(randHum)
#         self.readCO2(randCO2)
#         self.readlight(randlight)
#         self.readSoilMositure(randSoilMoisture)

    