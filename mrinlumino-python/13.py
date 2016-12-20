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

# ****************************************** challenge 1 ****************************************** 
print '********** Challenge 1 ************'

maze = []

maxSize = 48

# Create an open maze of size 100x100
for y in range(maxSize):
	row = ''
	for x in range(maxSize):
		str += ' '
	maze.append(str)


for y in range(maxSize):
	for x in range(maxSize):
		baseValue = x*x + 3*x + 2*x*y + y + y*y + puzzleInput
		binaryString = bin(baseValue)[2:]
		if binaryString.count('1') % 2 == 1:
			maze[y] = maze[y][:x] + '#' + maze[y][x+1:]


x = 1
y = 1
maze[1] = maze[1][:1] + 'o' + maze[1][2:]
currentDirection = 'D'
while x != 31 and y != 39:

	for s in maze:
		print s

	foundMyWay = 0

	if currentDirection == 'D': tryDirection = ['R','D','L','U']
	if currentDirection == 'R': tryDirection = ['U','R','D','L']
	if currentDirection == 'U': tryDirection = ['L','U','R','D']
	if currentDirection == 'L': tryDirection = ['D','L','U','R']

	orgX = x
	orgY = y

	for dir in range(4):
		if foundMyWay == 0: currentDirection = tryDirection[dir]

		# Test left
		if currentDirection == 'L' and foundMyWay == 0 and x > 0:
			if maze[y][x-1] == ' ' or maze[y][x-1] == 'o':
				foundMyWay = 1
				x -= 1


		# Test up
		if currentDirection == 'U'  and foundMyWay == 0 and y > 0:
			if maze[y-1][x] == ' ' or maze[y-1][x] == 'o':
				foundMyWay = 1
				y -= 1

		# Test right
		if currentDirection == 'R' and foundMyWay == 0 and x < maxSize:
			if maze[y][x+1] == ' ' or maze[y][x+1] == 'o':
				foundMyWay = 1
				x += 1


		# Test down
		if currentDirection == 'D'  and foundMyWay == 0 and y < maxSize:
			if maze[y+1][x] == ' ' or maze[y+1][x] == 'o':
				foundMyWay = 1
				y += 1

	print ('foundmywy=%s and walked to y:x %s:%s') % (foundMyWay, y,x)
	if maze[y][x] == ' ':
		maze[y] = maze[y][:x] + 'o' + maze[y][x+1:]
	else:
		maze[orgY] = maze[orgY][:orgX] + '.' + maze[orgY][orgX+1:]


	choice = raw_input("> ")
