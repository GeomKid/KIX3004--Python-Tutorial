TemperatureSensorReadingList = [
    "Sensor1/Lounge/2021.11.26 15:30/28.3",
    "Sensor2/Porch/2021.11.26 15:30/32.0",
    "Sensor2/Porch/2021.11.26 16:30/32.6",
]
temp_sensor_max = {}
for reading in TemperatureSensorReadingList:
    splitted = reading.split("/")
    saved_value = temp_sensor_max.get(splitted[0], None)
    temp_sensor_max[splitted[0]] = float(splitted[3]) if saved_value is None else max(float(splitted[3]), saved_value)

print(temp_sensor_max)
