from time import sleep, time
from datetime import datetime
class dataLogger():
    def __init__(self):
        self.filename = f'log{datetime.now()}.log'
        with open(self.filename, "a") as self.file:
            self.file.write("Time\t Temperature\t Humidity\t CO2\t light\t soil_Moisture\n")
    def logData(self,sensorData: dict):
        try:
           with open(self.filename, "a") as self.file:
            self.file.write(f'{int(time())}\t {sensorData["Temperature"]}\t {sensorData["Humidity"]}\t {sensorData["CO2"]}\t {sensorData["light"]}\t {sensorData["soil_Moisture"]}\n')
        except Exception as e:
            print("Error: ", e)

 

# testDataloger = dataLogger()
# tempdata = dict()
# tempdata["Temperature"] = 20
# tempdata["Humidity"] = 20
# tempdata["CO2"] = 20
# tempdata["light"] = 20
# tempdata["soil_Moisture"] = 20
# testDataloger.logData(tempdata)