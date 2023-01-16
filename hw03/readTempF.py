#!/usr/bin/env python3

# Created by: Martino Kim
# last updated date: 1/10/2023
# hw3 - Read temp in F(python)

import time
import smbus

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4a

while True:
    temp1 = bus.read_byte_data(address1, 0)
    temp2 = bus.read_byte_data(address2, 0)
    temp1 = ((temp1*9)/5) + 32
    temp2 = ((temp2*9)/5) + 32
    print("0x48: "+ str(temp1) + "F")
    print("0x4a: "+ str(temp2) + "F")
    
    #move the cursor 2 lines up to the beginning
    print('\033[F\033[K', end='')
    print("\033[F\033[K", end='')
    time.sleep(1)