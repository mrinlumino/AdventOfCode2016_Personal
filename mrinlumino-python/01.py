#!/usr/bin/python
# -*- coding: utf-8 -*-


print ''
print '***************************************************************************************'
print '*                                                                                     *'
print '*                              Advent of code 2016 1/12                               *'
print '*                             @MrInlumino - Anders Rosen                              *'
print '*                                                                                     *'
print '***************************************************************************************'
print ''


# Open input data file and read it into a string
fo = open('01.data','r')
rawinput = fo.read()
fo.close()

#remove all spaces
inputWIthoutSpaces = rawinput.replace(' ','')

#split the string into an array
route = inputWIthoutSpaces.split(',')

#Starting position
lat = 0 #N-S
long = 0 #E-W
direction = 'N'
visitedLocations = []
currentPositionInText = ('%s : %s') % (lat,long)
visitedLocations.append(currentPositionInText)
IHaveReturned = 0

# identify and execute each move
for move in route:
	turn = move[0]
	steps = int(move[1:])
	# execute turn
	if (turn == 'R' and direction == 'N') or (turn == 'L' and direction == 'S'): 
		direction = 'E'
	elif (turn == 'R' and direction == 'E') or (turn == 'L' and direction == 'W'): 
		direction = 'S'
	elif (turn == 'R' and direction == 'S') or (turn == 'L' and direction == 'N'): 
		direction = 'W'
	elif (turn == 'R' and direction == 'W') or (turn == 'L' and direction == 'E'): 
		direction = 'N'
	# do the walking
	for step in range(steps):
		if (direction == 'N'): lat = lat + 1
		if (direction == 'S'): lat = lat - 1
		if (direction == 'E'): long = long + 1
		if (direction == 'W'): long = long - 1
	
		#Have we been here before?
		currentPositionInText = ('%s : %s') % (lat,long)
		if (IHaveReturned == 0) and (currentPositionInText in visitedLocations):
			print ('Hey, I have been here (%s) before! It is %s blocks away') % (currentPositionInText,abs(lat) + abs(long))
			IHaveReturned = 1
		visitedLocations.append(currentPositionInText)

	#print('Turning %s and walking %s steps, ending up att lat/long %s/%s, directing %s') % (turn, steps, lat, long, direction)



print('Done walking and ended up at lat/long %s/%s, a total of %s blocks') % (lat,long,abs(lat) + abs(long))
	
print ''
print '***************************************************************************************'
print ''
