#!/usr/bin/env python3

import time

path = "/sys/class/hwmon/hwmon"
sens0 = path + "0/temp1_input"
sens1 = path + "1/temp1_input"
sens2 = path + "2/temp1_input"
temp0 = open(sens0, 'r')
temp1 = open(sens1, 'r')
temp2 = open(sens2, 'r')
# read sensor value infinately

# temp0.seek(0)
# temp1.seek(0)
# temp2.seek(0)
T0 = float(temp0.read()[:-1])/1000.0
time.sleep(0.1)
T1 = float(temp1.read()[:-1])/1000.0
time.sleep(0.1)
T2 = float(temp2.read()[:-1])/1000.0
print("T0:",T0,"T1:",T1,"T2:",T2)
# print("\033[F\033[K", end='')
