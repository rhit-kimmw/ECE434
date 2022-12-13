#!/usr/bin/env python3

yMax = int(input("Maximum rows:"))
xMax = int(input("Maximum columns:"))

grid = [[' ' for i in range(yMax)] for j in range(xMax)]

x=0
y=0 # current position

# # initialize the grid to all blanks
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         grid[i][j] = ' '
        
OriginalGrid = grid.copy()
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
    readLine = input("Direction> ")
    grid[y][x] = '*'
    
    if readLine == 'u':
        print("UP!")
        y = y-1
        if y<0:
            y = len(grid)-1
    elif readLine == 'd':
        print("Down!")
        y = y+1
        if y>=len(grid):
            y=0
    elif readLine == 'l':
        x = x-1
        if x<0:
            x=len(grid[y])-1
    elif readLine =='r':
        x = x+1 
        if x>=len(grid[y]):
            x=0 
    elif readLine == 'c':
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = ' '
        x = 0
        y = 0
    elif readLine == "close":
        exit()
    else:
        print("Wrong Input")
    grid[y][x] = '+'
    printGrid(grid)
    