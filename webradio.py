#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #Button Next
GPIO.setup(24, GPIO.IN) #Button Play
GPIO.setup(25, GPIO.IN) #Button Stop
GPIO.setup(18, GPIO.OUT) #LED Red
GPIO.setup(22, GPIO.OUT) #LED Green

GPIO.output(18,False) #Set both LED to off
GPIO.output(22,False) #in case of aborted script

GPIO.output(18,True) #Set to Red

while True:
    if (GPIO.input(24) == False):
        os.system('./play.sh &')
	GPIO.output(18,False) #Set to Green
	GPIO.output(22,True)	

    if (GPIO.input(25) == False):
        os.system('./stop.sh &')
	GPIO.output(18,True) #Set to Red
	GPIO.output(22,False) 

    if (GPIO.input(23)== False):
	GPIO.output(18,True) #Set to Orange
	GPIO.output(22,True)
        os.system('./next.sh &')
	sleep(1.5)		#Wait...
	GPIO.output(18,False)	#And green Again
 
    sleep(0.5);
