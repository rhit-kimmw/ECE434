#!/usr/bin/env python3

# Created by: Martino Kim
# updated date: 1/5/2023
# hw2 - control LED with buttons

import Adafruit_BBIO.GPIO as GPIO
import time

# initialize variables for pins
LED1 = "P9_15"
LED2 = "P9_16"
LED3 = "P9_17"
LED4 = "P9_18"

But1 = "P9_11"
But2 = "P9_12"
But3 = "P9_13"
But4 = "P9_14"

# setup the gpio pins
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)

GPIO.setup(But1,GPIO.IN)
GPIO.setup(But2,GPIO.IN)
GPIO.setup(But3,GPIO.IN)
GPIO.setup(But4,GPIO.IN)

while True:
    
    #if button is pressed, turn on corresponding LED
    if(GPIO.input(But1)):
        GPIO.output(LED1, GPIO.HIGH)
    else:
        GPIO.output(LED1, GPIO.LOW)
        
    if(GPIO.input(But2)):
        GPIO.output(LED2, GPIO.HIGH)
    else:
        GPIO.output(LED2, GPIO.LOW)
        
    if(GPIO.input(But3)):
        GPIO.output(LED3, GPIO.HIGH)
    else:
        GPIO.output(LED3, GPIO.LOW)
        
    if(GPIO.input(But4)):
        GPIO.output(LED4, GPIO.HIGH)  
    else:
        GPIO.output(LED4, GPIO.LOW)  
    #delay for 0.1seconds
    time.sleep(0.1)