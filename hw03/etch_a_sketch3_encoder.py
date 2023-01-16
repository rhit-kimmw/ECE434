#!/usr/bin/env python3

# Created by: Martino Kim
# updated date: 1/15/2022
# hw3 - Program for etch-a-sketch3 with 8x8 matrix 
# and two rotery encoders

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

# --------------------------------------------------------
# declare functions 

# function1 - print the grid
def printGrid(grid):
    print('   ', end= '')
    for i in range(len(grid[0])):
        print(str(i), end=' ')
    print()
    # print('   0 1 2 3 4 5 6 7\n')
    for i in range(len(grid)):
        print("{0}: ".format(i), end= '')
        for j in range(len(grid[i])):
            print("{0} ".format(grid[i][j]), end = '')
        print("\n")

# ---------------------------------------------------------
# setup

# Encoder1 -> Updown
EncPath1 = '/sys/bus/counter/devices/counter2/count0'
f = open(EncPath1+'/ceiling', 'w')
f.write('1000000')
f.close()
f = open(EncPath1+'/count', 'w')
f.write('500000')
f.close()
f = open(EncPath1+'/enable', 'w')
f.write('1')
f.close()
f = open(EncPath1+'/count','r')

# Encoder2 -> leftright
EncPath2 = '/sys/bus/counter/devices/counter1/count0'
f1 = open(EncPath2+'/ceiling', 'w')
f1.write('1000000')
f1.close()
f1 = open(EncPath2+'/count', 'w')
f1.write('500000')
f1.close()
f1 = open(EncPath2+'/enable', 'w')
f1.write('1')
f1.close()
f1 = open(EncPath2+'/count','r')

#use i2c bus 1
bus = smbus.SMBus(2)
matrix = 0x70 #matrix address 70 -> i2cdetect to find its address

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# initialize variables for buttons
But1 = "P9_11"
But2 = "P9_12"
But3 = "P9_13"
But4 = "P9_14"

# setup the gpio pins
GPIO.setup(But1,GPIO.IN)
GPIO.setup(But2,GPIO.IN)
GPIO.setup(But3,GPIO.IN)
GPIO.setup(But4,GPIO.IN)

#user input the size of matrix
yMax = int(input("Maximum rows:"))
xMax = int(input("Maximum columns:"))

#initialize the grid
grid = [[' ' for i in range(yMax)] for j in range(xMax)]
game =  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
x=0
y=0 # current position

# show a + at the current location
# current location on LED matrix -> Green
grid[y][x] = '+'
game[2*y] = game[2*y] | 2**x # turn on Green
game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
printGrid(grid)
bus.write_i2c_block_data(matrix, 0, game)

# oldY = updown encoder
# oldX = leftRight encoder
oldY = int(f.read())
oldX = int(f1.read())
#read user input
while(True):
    # set the encoder count pointer to original
    f.seek(0)
    f1.seek(0)
    # check if each buttons are pressed
    # up = GPIO.input(But1)
    # down = GPIO.input(But2)
    # right = GPIO.input(But3)
    # left = GPIO.input(But4)
    
    # use encoder to determine if curser moved
    newY = int(f.read())
    newX = int(f1.read())
    
    #setup clear button & close button
    clear = GPIO.input(But1)
    close = GPIO.input(But2)
    
    up = (oldY < newY)
    down = (oldY > newY)
    left = (oldX < newX)
    right = (oldX > newX)
    
    oldY = newY
    oldX = newX
    #if up and down button both pressed (but1 & but2)
    # -> clear the game
    if(clear):
        print("clear")
        # clear elements
        grid = [[' ' for i in range(yMax)] for j in range(xMax)]
        game =  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
        x=0
        y=0 # current position

        # show a + at the current location
        # current location on LED matrix -> Green
        grid[y][x] = '+'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
        printGrid(grid)
        # display game
        bus.write_i2c_block_data(matrix, 0, game)
        
    #if up and left button both pressed (but1 & but4) 
    # -> exit 
    elif(close):
        print("close")
        exit()
        
    
    # if up button pressed
    elif(up):
        print("Up!")
        # passed position -> Orange
        grid[y][x] = '*'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] | (2**x) # turn on Red
        y = y-1
        if y<0:
            y = len(grid)-1
        grid[y][x] = '+'
        # current position -> Green
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
        printGrid(grid)
        bus.write_i2c_block_data(matrix, 0, game)
        
    # if down button pressed
    elif(down):
        print("Down!")
        grid[y][x] = '*'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] | (2**x) # turn on Red
        y = y+1
        if y>=len(grid):
            y=0
        grid[y][x] = '+'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
        printGrid(grid)
        bus.write_i2c_block_data(matrix, 0, game)
    
    # if left button pressed
    elif(left):
        print("Left!")
        grid[y][x] = '*'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] | (2**x) # turn on Red
        x = x-1
        if x<0:
            x=len(grid[y])-1
        grid[y][x] = '+'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
        printGrid(grid)
        bus.write_i2c_block_data(matrix, 0, game)
    
    # if right button pressed
    elif(right):
        print("Right!")
        grid[y][x] = '*'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] | (2**x) # turn on Red
        x = x+1 
        if x>=len(grid[y]):
            x=0 
        grid[y][x] = '+'
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
        printGrid(grid)
        bus.write_i2c_block_data(matrix, 0, game)
        
    time.sleep(0.3)