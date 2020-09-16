'''
ModuleNotFoundError: No module named 'adafruit_max9744'

sudo pip3 install adafruit-circuitpython-max9744
pip3 install adafruit-circuitpython-max9744

run with (sudo will not work):
python3 speakerstest.py


i2cdetect -y 1

'''

# https://learn.adafruit.com/adafruit-20w-stereo-audio-amplifier-class-d-max9744/python-circuitpython
#
# Simple demo of the MAX9744 20W class D amplifier I2C control.
# This show how to set the volume of the amplifier.
# Author: Tony DiCola
import board
import busio
 
import adafruit_max9744
 
try:
	# Initialize I2C bus.
	i2c = busio.I2C(board.SCL, board.SDA)
	 
	# Initialize amplifier.
	amp = adafruit_max9744.MAX9744(i2c)
	# Optionally you can specify a different addres if you override the AD1, AD2
	# pins to change the address.
	# amp = adafruit_max9744.MAX9744(i2c, address=0x49)
	 
	# Setting the volume is as easy as writing to the volume property (note
	# you cannot read the property so keep track of volume in your own code if
	# you need it).
	amp.volume = 55  # Volume is a value from 0 to 63 where 0 is muted/off and
	# 63 is maximum volume.
	 
	# In addition you can call a function to instruct the amp to move up or down
	# a single volume level.  This is handy if you just have up/down buttons in
	# your project for volume:
	#amp.volume_up()  # Increase volume by one level.
	 
	#amp.volume_down()  # Decrease volume by one level.
except:
	print("Not able to talk with Amp via i2c")
	
import subprocess

subprocess.call("speaker-test -t wav -c 2 -l 2" , shell = True)
#from subprocess import call
#call(["speaker-test", "-t wav","-c 2"])

