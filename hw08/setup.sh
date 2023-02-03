#!/bin/bash

config-pin P9_31 out # need to set up to output.
export TARGET=hello.pru0
echo TARGET=$TARGET
echo out > /sys/class/gpio/gpio110/direction #gpio110 = P9_31. 