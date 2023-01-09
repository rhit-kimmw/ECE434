#!/usr/bin/env python3

# Created by: Martino Kim
# updated date: 1/5/2022
# hw2 - Program for etch-a-sketch2

import Adafruit_BBIO.GPIO as GPIO
import time

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

x=0
y=0 # current position

# show a + at the current location
grid[y][x] = '+'

# print the grid
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
    
printGrid(grid)

#read user input
while(True):
    
    grid[y][x] = '*'
    
    # check if each buttons are pressed
    up = GPIO.input(But1)
    down = GPIO.input(But2)
    right = GPIO.input(But3)
    left = GPIO.input(But4)
    
    #if up and down button both pressed (but1 & but2)
    # -> clear the game
    if(up and down):
        print("clear")
        # clear elements
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = ' '
        # set position to origin
        x = 0
        y = 0
        grid[y][x] = '+'
        #print the screen
        printGrid(grid)
        
    #if up and left button both pressed (but1 & but4) 
    # -> exit 
    elif(up and left):
        print("close")
        exit()
        
    
    # if up button pressed
    elif(up):
        print("Up!")
        y = y-1
        if y<0:
            y = len(grid)-1
        grid[y][x] = '+'
        printGrid(grid)
        
    # if down button pressed
    elif(down):
        print("Down!")
        y = y+1
        if y>=len(grid):
            y=0
        grid[y][x] = '+'
        printGrid(grid)
    
    # if left button pressed
    elif(left):
        print("Left!")
        x = x-1
        if x<0:
            x=len(grid[y])-1
        grid[y][x] = '+'
        printGrid(grid)
    
    # if right button pressed
    elif(right):
        print("Right!")
        x = x+1 
        if x>=len(grid[y]):
            x=0 
        grid[y][x] = '+'
        printGrid(grid)
        
    
    time.sleep(0.1)