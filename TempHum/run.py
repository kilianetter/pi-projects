import sys
import Adafruit_DHT as DHT
import time
import datetime as dt

from statistics import mean

T = []
RH = []


while True:
	now = dt.datetime.now()

	if (int(now.strftime("%S"))) == 0: 
		humidity , temperature = DHT.read_retry(11,4)

		
		T.append(temperature)
		RH.append(humidity)
		print(f'[{now.strftime("%Y-%m-%d - %H:%M:%S")}] Temperature array length: {len(T)} // Value: {T[len(T)-1]}')
		time.sleep(55)
	
	if (int(now.strftime("%M"))%5) == 0:
		mean_t = mean(T)
		mean_rh = mean(RH)
		print(f'[{now.strftime("%Y-%m-%d - %H:%M:%S")}] - Temp: {mean_t}°C - Humidity: {mean_rh}%')
		T = []
		RH = []
