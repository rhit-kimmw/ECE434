#!/usr/bin/env python3 

import smbus
import time

ad0 = '0053'
accel_path = "/sys/class/i2c-adapter/i2c-2/2-"+ad0+"/iio:device1/"
bus = smbus.SMBus(2)
fx = open(accel_path + 'in_accel_x_raw','r')
fy = open(accel_path + 'in_accel_y_raw','r')
fz = open(accel_path + 'in_accel_z_raw','r')
xmax = 0 
ymax = 0
zmax = 0
while(True):
    fx.seek(0)
    fy.seek(0)
    fz.seek(0)
    x = fx.read()[:-1]
    y = fy.read()[:-1]
    z = fz.read()[:-1]
    if(int(x) > xmax):
        xmax = int(x)
    if(int(y) > ymax):
        ymax = int(y)
    if(int(z) > zmax):
        zmax = int(z)
    print("x:",x,"y:",y,"z",z)
    print("max x,y,z:",xmax,ymax,zmax)
    print("\033[F\033[K", end='')
    print("\033[F\033[K", end='')
    time.sleep(0.1)