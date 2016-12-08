#!/usr/bin/python
# -*- coding: utf-8 -*-

# Advent of code 2016 6/12

# Open input data file and read it into a string
lines=[]
fo = open('indata.txt','r')
for line in fo:
	lines.append(line)
fo.close()


charCounterArray = []
for i in range(26):
    charCounterArray.append(0)


decrytpedMessage = ''
#iterate over each character
for charCounter in range(8):
	
	#reset charCounterArray
	for i in range(len(charCounterArray)):
		charCounterArray[i] = 0
	
	#iterate over all lines and count characters
	for line in lines:
		char = line[charCounter]
		charIndex = ord(char) - ord('a')
		#print ('Char: %s, index: %s') % (char,charIndex)
		charCounterArray[charIndex] = charCounterArray[charIndex] + 1

	highestCount = max(charCounterArray)
	charIndex = charCounterArray.index(highestCount)

	print charCounterArray
	decrytpedMessage = decrytpedMessage + chr(charIndex + ord('a'))

print ('Decrypted message: %s') % decrytpedMessage

# Gold star 2:
decrytpedMessage = ''
#iterate over each character
for charCounter in range(8):
	
	#reset charCounterArray
	for i in range(len(charCounterArray)):
		charCounterArray[i] = 0
	
	#iterate over all lines and count characters
	for line in lines:
		char = line[charCounter]
		charIndex = ord(char) - ord('a')
		#print ('Char: %s, index: %s') % (char,charIndex)
		charCounterArray[charIndex] = charCounterArray[charIndex] + 1

	lowestCount = min(charCounterArray)
	charIndex = charCounterArray.index(lowestCount)

	decrytpedMessage = decrytpedMessage + chr(charIndex + ord('a'))

print ('Decrypted message: %s') % decrytpedMessage
