#!/usr/bin/python
# -*- coding: utf-8 -*-

# Advent of code 2016 6/12

# Open input data file and read it into a string
lines=[]
fo = open('indata.txt','r')
for line in fo:
	lines.append(line.replace('\n','').strip(' '))
fo.close()

noOfPossibleTriangles = 0

for line in lines:
	sides = map(int,line.split())
	if (sides[0] + sides [1] > sides[2]) and (sides[1] + sides[2] > sides[0] ) and (sides[0] + sides[2] > sides[1]):
		noOfPossibleTriangles += 1
#		print str(sides) + ': True'
#	else: print str(sides) + ': False'

print 'Number of possible triangles: %s' % str(noOfPossibleTriangles)


# problem 2

#convert to ints
intLines = []
for line in lines:
	intLines.append(map(int,line.split()))


print len(lines)
print len(intLines)

noOfPossibleTriangles = 0

for counter in range(len(intLines)/3):
#	print ('[%s,%s,%s]') % (intLines[counter+0][0],intLines[counter+1][0],intLines[counter+2][0])
	print intLines[counter*3+0][0]

	if (intLines[counter*3+0][0] + intLines[counter*3+1][0] > intLines[counter*3+2][0]) and (intLines[counter*3+1][0] + intLines[counter*3+2][0] > intLines[counter*3+0][0]) and (intLines[counter*3+0][0] + intLines[counter*3+2][0] > intLines[counter*3+1][0]):
#		print ('true')
		noOfPossibleTriangles += 1
#	else:
#		print ('false')		

#	print ('[%s,%s,%s]') % (intLines[counter+0][1],intLines[counter+1][1],intLines[counter+2][1])
	if (intLines[counter*3+0][1] + intLines[counter*3+1][1] > intLines[counter*3+2][1]) and (intLines[counter*3+1][1] + intLines[counter*3+2][1] > intLines[counter*3+0][1]) and (intLines[counter*3+0][1] + intLines[counter*3+2][1] > intLines[counter*3+1][1]):
#		print ('true')
		noOfPossibleTriangles += 1
#	else:
#		print ('false')		

#	print ('[%s,%s,%s]') % (intLines[counter+0][2],intLines[counter+1][2],intLines[counter+2][2])
	if (intLines[counter*3+0][2] + intLines[counter*3+1][2] > intLines[counter*3+2][2]) and (intLines[counter*3+1][2] + intLines[counter*3+2][2] > intLines[counter*3+0][2]) and (intLines[counter*3+0][2] + intLines[counter*3+2][2] > intLines[counter*3+1][2]):
#		print ('true')
		noOfPossibleTriangles += 1
#	else:
#		print ('false')		

print 'Number of possible triangles in case 2: %s' % str(noOfPossibleTriangles)

