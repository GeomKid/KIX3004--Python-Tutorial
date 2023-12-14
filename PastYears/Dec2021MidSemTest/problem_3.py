temp_sensor_dict = {}
TemperatureSensorReading = "Sensor1/Lounge/2021.11.26 15:30/28.3"

splitted = TemperatureSensorReading.split("/")

temp_sensor_dict["SENSORID"] = splitted[0]
temp_sensor_dict["LOCATION"] = splitted[1]
temp_sensor_dict["DATETIME"] = splitted[2]
temp_sensor_dict["TEMPERATURE"] = float(splitted[3])

print(temp_sensor_dict)
