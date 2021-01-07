import sys
import Adafruit_DHT as DHT
import time
import datetime as dt


while True:
	now = dt.datetime.now()

	if (int(now.strftime("%S"))) == 0: 
		humidity , temperature = DHT.read_retry(11,4)

		print(f'[{now.strftime("%Y-%m-%d - %H:%M:%S")}] - Temp: {temperature}°C - Humidity: {humidity}%')
		time.sleep(55)
