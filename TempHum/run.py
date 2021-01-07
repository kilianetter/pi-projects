import sys
import Adafruit_DHT as DHT
import time
import datetime as dt

from statistics import mean

T = []
RH = []

function avg(lst):
	average = sum(lst) / len(lst)
	return average

while True:
	now = dt.datetime.now()

	if (int(now.strftime("%S"))) == 0: 
		humidity , temperature = DHT.read_retry(11,4)

		
		T.append(temperature)
		RH.append(humidity)
		print(f'[{now.strftime("%Y-%m-%d - %H:%M:%S")}] Temperature array length: {len(T)} // Value: {T[len(T)-1]}')
		time.sleep(55)
	
	if (int(now.strftime("%M"))%5) == 0:
		mean_t = avg(T)
		mean_rh = avg(RH)
		print(f'[{now.strftime("%Y-%m-%d - %H:%M:%S")}] - Temp: {mean_t}°C - Humidity: {mean_rh}%')
		T = []
		RH = []
