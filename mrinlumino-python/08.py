#!/usr/bin/python
# -*- coding: utf-8 -*-


print ''
print '***************************************************************************************'
print '*                                                                                     *'
print '*                              Advent of code 2016 8/12                               *'
print '*                             @MrInlumino - Anders Rosen                              *'
print '*                                                                                     *'
print '***************************************************************************************'
print ''


# ****************************************** challenge 1 ****************************************** 

noOfColumns = 50
noOfRows = 6

# Open input data file and read it into a list of strings
lines=[]
fo = open('08.data','r')
for line in fo:
	lines.append(line.replace('\n',''))
fo.close()

# create a pixel representation in an array with 6*50 position, filled witn a 0 identifying unlit pixels
pixels = []
for row in range(noOfRows):
	column = []
	for cols in range (noOfColumns):
		column.append(0)
	pixels.append(column)

#print pixels


for instruction in lines:
	print ''
	print ('Instruction: % s') % (instruction)
	if instruction[0:4] == 'rect':
		#Create a rectangle of lit lights
		#print 'Lighting rectange'
		size = map(int,instruction[5:].split('x'))
		for y in range(size[1]):
			for x in range(size[0]):
				pixels[y][x]=1


	if instruction[:13] == 'rotate column':
		for l in pixels: print l
		#print 'Rotating column'
		#print instruction[14:].split(' ')
		col = int(instruction[14:].split(' ')[0][2:])
		moves = int(instruction[14:].split(' ')[2])
		for counter in range(moves):
			#Shifts the lights one row down
			replacedPixel = pixels[5][col]
			for y in range(6):
				tempPixel = pixels[y][col]
				pixels[y][col] = replacedPixel
				replacedPixel = tempPixel
		print ''
		for l in pixels: print l
		#raw_input("Press Enter to continue...")	

	if instruction[0:10] == 'rotate row':
		#print pixels

#		print 'Rotating row'
		row = int(instruction[13:14])
		moves = int(instruction[18:])
		for counter in range(moves):
			#Shift the lights one column
			replacedPixel = pixels[row][49]
			for x in range(50):
				tempPixel = pixels[row][x]
				pixels[row][x] = replacedPixel
				replacedPixel = tempPixel
				#print pixels[row]
#		print pixels
#		raw_input("Press Enter to continue...")	


# count pixels
noOfLitPixels = 0 
for y in range(6): 
	for x in range(50): 
		noOfLitPixels += pixels[y][x]

print ('Total number of lit pixels: %s') % noOfLitPixels

print ''
print '***************************************************************************************'
print ''


