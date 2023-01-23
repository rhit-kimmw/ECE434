#!/bin/bash
# Accelerometer setup
# Martino Kim

cd /sys/class/i2c-adapter/i2c-2

if [ ! -d "2-0053" ]
then
    echo adxl345 0x53 > new_device 
fi 
