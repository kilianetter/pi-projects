import sys
import Adafruit_DHT as DHT
import time
import datetime as dt

from statistics import mean

T = []
RH = []

def avg(lst):
	print(sum(lst))
	print(len(lst)
	average = sum(lst) / len(lst)
	return average

while True:
	now = dt.datetime.now()

	if (int(now.strftime("%S"))) == 0: 
		humidity , temperature = DHT.read_retry(11,4)

		
		T.append(temperature)
		RH.append(humidity)
		print(f'[{now.strftime("%Y-%m-%d - %H:%M:%S")}] Temperature array length: {len(T)} // Value: {T[len(T)-1]}')
		      
		if (int(now.strftime("%M"))%3) == 0:
			mean_t = avg(T)
			mean_rh = avg(RH)
			print(f'[{now.strftime("%Y-%m-%d - %H:%M:%S")}] - Temp: {mean_t}°C - Humidity: {mean_rh}%')
			T = []
			RH = []
		time.sleep(55)
	

