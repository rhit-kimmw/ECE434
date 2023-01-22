#!/bin/bash
# TMP101 temperature with kernel
# Martino Kim

cd /sys/class/i2c-adapter/i2c-2

if [ ! -d "2-0048" ]
then
    echo tmp101 0x48 > new_device
fi
cd 2-0048/hwmon/hwmon0

while true
do
    temp=$(cat temp1_input)
    temp1=$((temp/1000))
    temp2=$((temp%1000))

    printf "Temp: $temp1.$temp2 °C\r"
done