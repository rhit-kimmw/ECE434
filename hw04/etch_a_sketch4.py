#!/usr/bin/env python3 

import gpiod
import sys
import time
import smbus
from flask import Flask, render_template, request

# define 
app = Flask(__name__)

bus = smbus.SMBus(2)
matrix = 0x70 #matrix address 70 -> i2cdetect to find its address

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

game =  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
maxX = 1
maxY = 1
x = 0
y = 0
game[2*y] = game[2*y] | 2**x # turn on Green
game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
bus.write_i2c_block_data(matrix, 0, game) # display game on matrix

@app.route("/")
def index():
    templateData = {
        'title' : 'Etch-A-Sketch!',
        'row' : maxY,
        'column' : maxX
        }
    return render_template('game.html', **templateData)

@app.route("/<action>")
def action(action):
    
    global game
    global x
    global y
    global maxX
    global maxY
    #6 actions -> up, down, left, right, clear, close
    if action == "up":
        #past position -> orange
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] | (2**x)
        
        #set y (up)
        y = y-1
        if y<0:
            y = maxY-1
        
        #current position -> green
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] & ~(2**x)
        
        #print the result on LED matrix
        bus.write_i2c_block_data(matrix, 0, game)
    if action == 'down':
        #past position -> orange
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] | (2**x)
        
        #set y (down)
        y = y+1
        if y>=maxY:
            y = 0
        
        #current position -> green
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] & ~(2**x)
        
        #print the result on LED matrix
        bus.write_i2c_block_data(matrix, 0, game)
        
    if action == 'left':
        #past position -> orange
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] | (2**x)
        
        #set x (left)
        x = x-1
        if x<0:
            x = maxX-1
        
        #current position -> green
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] & ~(2**x)
        
        #print the result on LED matrix
        bus.write_i2c_block_data(matrix, 0, game)

    if action == 'right':
        #past position -> orange
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] | (2**x)
        
        #set x (right)
        x = x+1
        if x>=maxX:
            x = 0
        
        #current position -> green
        game[2*y] = game[2*y] | 2**x
        game[2*y+1] = game[2*y+1] & ~(2**x)
        
        #print the result on LED matrix
        bus.write_i2c_block_data(matrix, 0, game)
        
    if action == 'clear':
        #clear the game
        game = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
        #clear the position
        x = 0
        y = 0
        game[2*y] = game[2*y] | 2**x # turn on Green
        game[2*y+1] = game[2*y+1] & ~(2**x) # turn off Red
        #print the result on LED matrix
        bus.write_i2c_block_data(matrix, 0, game)
        
    if action == 'col+1':
        if maxX < 8:
            maxX += 1
        else:
            maxX = 8
        
        
    if action == 'col-1':
        if maxX > 1:
            maxX -= 1
        else:
            maxX = 1
        
    if action == 'row+1':
        if maxY < 8:
            maxY += 1
        else:
            maxY = 8    
    if action == 'row-1':
        if maxY > 1:
            maxY -= 1
        else:
            maxY = 1    
    templateData = {
        'title' : 'Etch-A-Sketch!',
        'row' : maxY,
        'column' : maxX
    }
    return render_template('game.html', **templateData)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8081, debug = True)