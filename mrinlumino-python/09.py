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
inputData = fo.read()
fo.close()

# ****************************************** challenge 1 ****************************************** 
rawinput = inputData
output = ''
loop = 0

#identify the first instruction
startMarker = rawinput.find('(')


while startMarker > -1:
	# Are there any characters before the next start marker, then add these to the output and remove them from the input
	if startMarker > 0:
		output += rawinput[:startMarker]
		rawinput = rawinput[startMarker:]

	endMarker = rawinput.find(')')
	instruction = map(int,rawinput[1:endMarker].split('x'))
	if loop > 3: print instruction 

	rawinput = rawinput[endMarker+1:]
	

	for iteration in range(instruction[1]):
		output += rawinput[:instruction[0]]


	rawinput = rawinput[instruction[0]:]

	startMarker = rawinput.find('(')

#Add last remaining part of the string
output += rawinput

print 'Resulting string length (Challenge 1): % s' % len(output)



# ****************************************** challenge 2 ****************************************** 
rawinput = inputData
#rawinput = '(9x3)CD(2x2)EFAB(9x3)CD(2x2)EF'
#rawinput = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
totalLenght = 0


def CalculateDecodedStringLengh(inString):
	lengthOfString = 0
	
	#print ''
	#print ('CalculateDecodedStringLengh - Instring: %s') % inString

	#Find any instructions
	while inString.find('(') > -1:

		# Remove any starting characters
		if inString.find('(')>0:
			lengthOfString += inString.find('(')
			inString = inString[inString.find('('):]
			#print ('CalculateDecodedStringLengh - Found starting chars, trimed string: %s, lenght now: %s') % (inString, lengthOfString)

		endMarker = inString.find(')')
		instruction = map(int,inString[1:endMarker].split('x'))

		#print ('CalculateDecodedStringLengh - Instruction: %s') % instruction

		#remove instruction string
		inString = inString[endMarker+1:]		
		#print ('CalculateDecodedStringLengh - instruction removed: %s') % inString

		# Extract the string to be repeated
		repeatString = inString[:instruction[0]]
		#print ('CalculateDecodedStringLengh - repeat string: %s') % repeatString

		# Iterate the instructed amount of times
		for i in range(instruction[1]):
			lengthOfString += CalculateDecodedStringLengh(repeatString)
			#print ('CalculateDecodedStringLengh - iteration: %s') % i

		#remove the repeated string
		inString = inString[instruction[0]:]	
		#print ('CalculateDecodedStringLengh - instring: %s') % inString
	
	# Add possible remaining characters
	lengthOfString += len(inString)

	# Return the calculated string length
	return lengthOfString

# print ''
# print CalculateDecodedStringLengh('AB(9x3)CD(2x2)EFAB(9x3)CD(2x2)EF')



#identify the first instruction
startMarker = rawinput.find('(')

while startMarker > -1:
	# Are there any characters before the next start marker, then count these and remove them from the string
	#print ('Current string are now: %s') % rawinput
	if startMarker > 0:
		totalLenght += startMarker
		rawinput = rawinput[startMarker:]
		#print ('Starting chars removed: %s, total lenght: %s') % (rawinput,totalLenght)

	# Find the end paranthesis
	endMarker = rawinput.find(')')

	# Extract the instruction
	instruction = map(int,rawinput[1:endMarker].split('x'))

	# Remove the instruction from the string
	rawinput = rawinput[endMarker+1:]
	#print ('instruction  removed: %s, instruction: %s') % (rawinput, instruction)

	for iteration in range(instruction[1]):
		print ('Current lenght: %s, iteration: %s/%s') % (totalLenght,iteration,instruction[1]-1)
		totalLenght += CalculateDecodedStringLengh(rawinput[:instruction[0]])
		#print ('Iteration %s total lengh: %s') % (iteration,totalLenght)

	# Remove the substring
	rawinput = rawinput[instruction[0]:]
	print ('Remaining string length: %s') % len(rawinput)
	#print ('rawinput after first instruction string removed: %s') % rawinput

	# Find any more start paranthesis
	startMarker = rawinput.find('(')


	#raw_input("Press Enter to continue...")
#Add last remaining part of the string
totalLenght += len(rawinput)

#print ''
print ('Total lenght of decoded string (Challenge 2): %s') % totalLenght

