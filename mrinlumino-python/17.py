#!/usr/bin/python
# -*- coding: utf-8 -*-


print ''
print '***************************************************************************************'
print '*                                                                                     *'
print '*                              Advent of code 2016 17/12                               *'
print '*                             @MrInlumino - Anders Rosen                              *'
print '*                                                                                     *'
print '***************************************************************************************'
print ''

import hashlib
m = hashlib.md5()

# ****************************************** challenge 1 ****************************************** 
print '********** Challenge 1 ************'

puzzleInput = 'gdjjyniy'

# Define a step in the maze
# [row, column, hash, Up, Down, Left, Right, Done]
steps = []
steps.append([1,1,'gdjjyniy','','','','',0])

pathFound = 0
stopcounter = 0
path = ''

while pathFound == 0 and stopcounter<100:
	NumberOfSteps = len(steps)
	for stepCount in range(NumberOfSteps):
		# Check to see if we reached our goal
		if steps[stepCount][0] == 4 and steps[stepCount][1] == 4: 
			pathFound = 1
			path = steps[stepCount][2]

		if steps[stepCount][7] == 0:
			md5Hash = hashlib.md5(steps[stepCount][2]).hexdigest()
			
			#Can I move up?
			if steps[stepCount][0] > 1:
				if ord(md5Hash[0]) >= ord('b') and ord(md5Hash[0]) <= ord('f'):
					steps.append([steps[stepCount][0]-1,steps[stepCount][1],steps[stepCount][2] + 'U','','','','',0])
			
			#Can I move down?
			if steps[stepCount][0] < 4:
				if ord(md5Hash[1]) >= ord('b') and ord(md5Hash[1]) <= ord('f'):
					steps.append([steps[stepCount][0]+1,steps[stepCount][1],steps[stepCount][2] + 'D','','','','',0])
			
			#Can I move left?
			if steps[stepCount][1] > 1:
				if ord(md5Hash[2]) >= ord('b') and ord(md5Hash[2]) <= ord('f'):
					steps.append([steps[stepCount][0],steps[stepCount][1]-1,steps[stepCount][2] + 'L','','','','',0])
			
			#Can I move right?
			if steps[stepCount][1] < 4:
				if ord(md5Hash[3]) >= ord('b') and ord(md5Hash[3]) <= ord('f'):
					steps.append([steps[stepCount][0],steps[stepCount][1]+1,steps[stepCount][2] + 'R','','','','',0])

			# This step is now done
			steps[stepCount][7] = 1

	stopcounter += 1


print path

