#!/usr/bin/env python3

# Created by: Martino Kim
# last updated date: 1/10/2023
# hw3 - set T_high & T_low(python) 
# alert when temperature gets off the temperature limit

import smbus
import time 
import Adafruit_BBIO.GPIO as GPIO

# set up a bus
bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4a 
t_low = 25
t_high = 27

# set up GPIO alert pins as input
alert1 = "P9_21"
alert2 = "P9_22"
GPIO.setup(alert1, GPIO.IN)
GPIO.setup(alert2, GPIO.IN)
GPIO.add_event_detect(alert1, GPIO.RISING)
GPIO.add_event_detect(alert2, GPIO.RISING)

bus.write_byte_data(address1, 1, 0b11100110)
bus.write_byte_data(address1, 2, t_low)
bus.write_byte_data(address1, 3, t_high)

bus.write_byte_data(address2, 1, 0b11100110)
bus.write_byte_data(address2, 2, t_low)
bus.write_byte_data(address2, 3, t_high)


print("start")
print("limit: " + str(t_low) + "~" + str(t_high))
while True:
    
    detected1 = GPIO.event_detected(alert1)
    detected2 = GPIO.event_detected(alert2)
    if(detected1):
        temp1 = bus.read_byte_data(address1, 0)
        print("detected")
        print(" 0x48: " + str(temp1) + "C")
        time.sleep(1)
        print("\033[F\033[K", end='')
        print("\033[F\033[K", end='')
    if(detected2):
        temp2 = bus.read_byte_data(address2, 0)
        print("detected")
        print(" 0x4a: " + str(temp2) + "C")
        time.sleep(1)
        print("\033[F\033[K", end='')
        print("\033[F\033[K", end='')
        