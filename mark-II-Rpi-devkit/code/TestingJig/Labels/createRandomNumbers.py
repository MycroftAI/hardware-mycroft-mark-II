import csv
import datetime
import random


randomSet = random.sample(range(0x00001000, 0x0000FFFF), 500)

with open('MycroftSerialNumbers.csv', mode='w') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	ct = datetime.datetime.now() 
	print("current time:-", ct) 
	randomSet.sort()
	
	for num  in randomSet:
		toUpper =("%08x" % ( num)).upper()
		print( toUpper)
		csv_writer.writerow([toUpper, ct])
