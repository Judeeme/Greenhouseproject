# import board
# import adafruit_dht
import Adafruit_DHT as DHT
import random
from time import sleep, time
import json
from math import pow
import RPi.GPIO as GPIO
# import Adafruit_ADS1x15 as ADC
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class sensors():
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1015(self.i2c)
        self.co2Pin = 1
        # self.adc = ADC.ADS1115()
        self.gain = 1
        self.tempHumPin = 26
        self.TempHum = DHT.DHT22
        self.soilPin = 0
        self.lightPin = 2
        # self.setupGPIO()
    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.soilPin, GPIO.IN)
        sleep(2)
    def readTempHumSensor(self):
        humidity, temperature = DHT.read_retry(self.TempHum,self.tempHumPin)
        # print(f"Temp={temperature:0.1f}°C Humidity={humidity:0.1f}%")

        return[float(f'{temperature:0.1f}'),float(f'{humidity:0.1f}')]
    def readSoilSensor(self):
        self.soil = AnalogIn(self.ads, ADS.P1)
        # print(self.soil.value)
        soilVal = (self.soil.value)/1000
        # pass
        # soilVal = self.adc.read_adc(self.soilPin, gain=self.gain)/1000
        return[(float(f'{soilVal:0.5f}'))]
        
        # sleep(0.5)
    def readCO2Sensor(self):
        self.CO2 = AnalogIn(self.ads, ADS.P2)
        # print(self.CO2.value)
        co2Val = (self.CO2.value)/1000
        # pass
        # co2Val = self.adc.read_adc(self.co2Pin,gain=self.gain)/1000
        return[(float(f'{co2Val:0.5f}'))]
        # sleep(0.5)
    def readLightSensor(self):
        self.light = AnalogIn(self.ads, ADS.P0)
        # print(self.light.value)
        lightVal = (self.light.value)/1000
        # pass
        # lightVal = self.adc.read_adc(self.lightPin,gain=self.gain)/1000
        return[(float(f'{lightVal:0.5f}'))]
    def readSensors(self):
        try:
            tempHum = self.readTempHumSensor()
            # sleep(1)
            soil = self.readSoilSensor()
            # sleep(1)
            CO2 = self.readCO2Sensor()
            # sleep(1)
            light = self.readLightSensor()
            # sleep(1)
            sensorval = [tempHum[0],tempHum[1],soil[0],CO2[0],light[0]]
            return sensorval
        except:
            print("Error reading")
            return [0,0,0,0,0]  
    # def adc1115(self):
    #     # sbc = rgpio.sbc()
    #     adc = lg_ads1x15.ads1115(sbc, 1, 0x48)
    #     adc.set_voltage_range(3.3)
    #     adc.set_sample_rate(0) # minimum sampling rate
    #     adc.set_channel(adc.A0)
    #     end_time = time() + 120
    #     while time() < end_time:
    #         print(adc.read_voltage())
    #         sleep(5)
    #     adc.close()

# Testsensor = sensors()
# Testsensor.readTempHumSensor()
# Testsensor.readCO2Sensor()
# Testsensor.readLightSensor()
# Testsensor.readSoilSensor()
# for i in range(5):
#     print(Testsensor.readSensors())
#     sleep(1)
# print(Testsensor.readTempSensor())
# print("Testing Sensors")
# print(f'CO2: {Testsensor.readCO2Sensor()}')
# print(f'Soil: {Testsensor.readSoilSensor()}')
# print(f'Light: {Testsensor.readLightSensor()}')
# print(f'Temp Hum: {Testsensor.readTempHumSensor()}')
# Testsensor.adc1115()