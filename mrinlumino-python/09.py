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


# Open input data file and read it into a string
fo = open('09.data','r')
rawinput = fo.read()
fo.close()

print rawinput

output = ''

#identify the first instruction
startMarker = rawinput.find('(')

while startMarker > -1:
	# Are there any characters before the next start marker, then add these to the output and remove them from the input
	if startMarker > 0:
		output += rawinput[:startMarker]
		rawinput = rawinput[startMarker:]

	endMarker = rawinput.find(')')
	instruction = rawinput[1:endMarker].split('x')
	print instruction 

	#remove first instruction
	rawinput = rawinput[endMarker+1:]
	print rawinput

	startMarker = -1
