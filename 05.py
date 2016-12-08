#!/usr/bin/python
# -*- coding: utf-8 -*-

# Advent of code 2016 5/12

import hashlib
m = hashlib.md5()


puzzleInput = 'reyedfim'
codeString = '********'

counter = 0
while codeString.find('*') > -1:
	puzzleInputWithNumbers = puzzleInput + str(counter)
	#print puzzleInputWithNumbers
	#m.update(puzzleInputWithNumbers)
	#mdFiveString = m.hexdigest()
	mdFiveString= hashlib.md5(puzzleInputWithNumbers).hexdigest()
	if mdFiveString[0:5] == '00000':
		if ord(mdFiveString[5]) in range(ord('0'),ord('8')):
			position = int(mdFiveString[5])
			if codeString[position] == '*':
				codeString = codeString[:position] + mdFiveString[6] + codeString[position+1:]
				print codeString
		#codeString += mdFiveString[5]
		print ('Tested string: % s, MD5 hash: %s, identified char: %s') % (puzzleInputWithNumbers,mdFiveString,mdFiveString[5])
		
	counter += 1

print ('Identified code: %s') % codeString