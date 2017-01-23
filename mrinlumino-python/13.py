#!/usr/bin/python
# -*- coding: utf-8 -*-


print ''
print '***************************************************************************************'
print '*                                                                                     *'
print '*                              Advent of code 2016 13/12                               *'
print '*                             @MrInlumino - Anders Rosen                              *'
print '*                                                                                     *'
print '***************************************************************************************'
print ''


puzzleInput = 1364

# ****************************************** challenge 1 *****************

print '********** Challenge 1 ************'

# Solved the maze using the Lee algorithm
# https://en.wikipedia.org/wiki/Lee_algorithm

maze = []

# Create a big enough maze to hold the solution
maxSize = 50

# Create an open maze filled with spaces
for y in range(maxSize):
    row = []
    for x in range(maxSize):
        row.append(' ')
    maze.append(row)

# Build the labyrinth
for y in range(maxSize):
    for x in range(maxSize):
        baseValue = x * x + 3 * x + 2 * x * y + y + y * y + puzzleInput
        binaryString = bin(baseValue)[2:]
        if binaryString.count('1') % 2 == 1:
            maze[y][x] = '#'

for y in range(maxSize):
    print ''.join(maze[y])

# Function that marks open positions around a specified coordinate with weighted values
# Calls itself recursively until every available position is weighted


def markNeighbors(posY, posX, value):
    if posX > 0:
        if maze[posY][posX - 1] == ' ':
            maze[posY][posX - 1] = value
            markNeighbors(posY, posX - 1, value + 1)
    if posX < maxSize - 1:
        if maze[posY][posX + 1] == ' ':
            maze[posY][posX + 1] = value
            markNeighbors(posY, posX + 1, value + 1)
    if posY > 0:
        if maze[posY - 1][posX] == ' ':
            maze[posY - 1][posX] = value
            markNeighbors(posY - 1, posX, value + 1)
    if posY < maxSize - 1:
        if maze[posY + 1][posX] == ' ':
            maze[posY + 1][posX] = value
            markNeighbors(posY + 1, posX, value + 1)

# A function that finds the position with the lowest weight value and
# returns its position


def findNextPosition(curPos):
    y = curPos[0]
    x = curPos[1]
    bestX = x
    bestY = y
    minVal = 1000
    if y > 0:
        if maze[y - 1][x] < minVal:
            bestY = y - 1
            bestX = x
            minVal = maze[y - 1][x]
            # print minVal
    if y < maxSize - 1:
        if maze[y + 1][x] < minVal:
            bestY = y + 1
            bestX = x
            minVal = maze[y + 1][x]
    if x > 0:
        if maze[y][x - 1] < minVal:
            bestX = x - 1
            bestY = y
            minVal = maze[y][x - 1]
    if x < maxSize - 1:
        if maze[y][x + 1] < minVal:
            bestX = x + 1
            bestY = y
            minVal = maze[y][x + 1]
    return [bestY, bestX]


# Starting position
maze[1][1] = 0

# Call the recursive function to fill the maze with weighted values
markNeighbors(1, 1, 1)

# Start from the target position and walk backwards using the lowest
# available value path
currentPosition = [39, 31]
numberOfSteps = 0

# Walk until were back at the starting position
while currentPosition != [1, 1]:
    # Increase the number of steps
    numberOfSteps += 1
    currentPosition = findNextPosition(currentPosition)

print 'Challenge 1: Number of steps through the maze was: %s' % numberOfSteps


# ****************************************** challenge 2 *****************
# CURRENTLY NOT WORKING!
print '\n********** Challenge 2 ************'

NoOfValues = 0
for y in range(maxSize):
    for x in maze[y]:
        if x != ' ' and x != '#':
            if x <= 51:
                NoOfValues += 1

print NoOfValues
