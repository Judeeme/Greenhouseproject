#!/usr/bin/python 
import mariadb 

class db():
    def __init__(self):
        self.conn = self.connect()
    def connect(self):
        self.dbconn = mariadb.connect(
            user = "root",
            password = "123456",
            database = "greenhouse",
            host = "localhost"
            )
        mydb = self.dbconn.cursor()
        return mydb
    def droptable(self):
        self.conn.execute("DROP TABLE Sensors")
    def createtable(self):
        self.conn.execute("CREATE TABLE Sensors (Temperature FLOAT, Humidity FLOAT, Soil FLOAT, CO2 FLOAT, Light FLOAT, Time FLOAT,sensorID int NOT NULL AUTO_INCREMENT, PRIMARY KEY(sensorID))")
        self.conn.execute("DESCRIBE Sensors")
        # for x in self.conn:
            # print(x)
    def setValues(self,values):
        val = []
        for key,value in values.items():
            val.append(value)
        val = tuple(val)
        self.conn.execute("INSERT INTO Sensors (Temperature,Humidity,Soil,CO2,Light,Time) VALUES (%s,%s,%s,%s,%s,%s)",(val))
        self.dbconn.commit()
    def select(self):
        self.conn.execute("SELECT Temperature, Humidity, sensorID FROM Sensors")
        for x in self.conn:
            print(x)


# someDict = {"Temperature":12, "Humidity": 21, "Soil":31, "CO2":13, "Light": 31, "Time":123}
mydb = db()
# mydb.droptable()
# mydb.createtable()
# mydb.setValues(someDict)
mydb.select()



# alist = []
# for key,value in someDict.items():
#     alist.append(key)
# print(alist)
      
#retrieving information 
# some_name = "Georgi" 
# cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,)) 

# for first_name, last_name in cur: 
#     print(f"First name: {first_name}, Last name: {last_name}")
    
# #insert information 
# try: 
#     cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
# except mariadb.Error as e: 
#     print(f"Error: {e}")

# conn.commit() 
# print(f"Last Inserted ID: {cur.lastrowid}")
    
# conn.close()