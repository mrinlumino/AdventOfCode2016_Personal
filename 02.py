#!/usr/bin/python
# -*- coding: utf-8 -*-

# Advent of code 2016 2/12

# Open input data file and read it into a string
lines=[]
fo = open('indata.txt','r')
for line in fo:
	lines.append(line)
	#print ('>%s') % line
fo.close()


activeKey = '5'
keyCode = ''

for line in lines:
	for char in line:
		#result = 1
		if (char == 'U' and activeKey == '4') or (char == 'L' and activeKey == '2'): 
			activeKey = '1'
		#result = 2
		elif (char == 'U' and activeKey == '5') or (char == 'R' and activeKey == '1') or (char == 'L' and activeKey=='3'):
			activeKey = '2'
		#result = 3
		elif (char == 'U' and activeKey == '6') or (char == 'R' and activeKey == '2'):
			activeKey = '3'
		#result = 4
		elif (char == 'U' and activeKey == '7') or (char == 'L' and activeKey == '5') or (char == 'D' and activeKey=='1'):
			activeKey = '4'		
		#result = 5
		elif (char == 'U' and activeKey == '8') or (char == 'R' and activeKey == '4') or (char == 'L' and activeKey=='6')or (char == 'D' and activeKey=='2'):
			activeKey = '5'		
		#result = 6
		elif (char == 'U' and activeKey == '9') or (char == 'R' and activeKey == '5') or (char == 'D' and activeKey=='3'):
			activeKey = '6'	
		#result = 7
		elif (char == 'D' and activeKey == '4') or (char == 'L' and activeKey == '8') :
			activeKey = '7'		
		#result = 8
		elif (char == 'D' and activeKey == '5') or (char == 'R' and activeKey == '7') or (char == 'L' and activeKey=='9'):
			activeKey = '8'		
		#result = 9
		elif (char == 'D' and activeKey == '6') or (char == 'R' and activeKey == '8'):
			activeKey = '9'
	keyCode = keyCode + str(activeKey)
	
print ('Key code: %s') % keyCode


# Part 2
activeKey = '5'
keyCode = ''

for line in lines:
	for char in line:
		#result = 1
		if (char == 'U' and activeKey == '3'): 
			activeKey = '1'
		#result = 2
		elif (char == 'U' and activeKey == '6') or (char == 'L' and activeKey == '3'):
			activeKey = '2'
		#result = 3
		elif (char == 'D' and activeKey == '1') or (char == 'R' and activeKey == '2') or (char == 'L' and activeKey == '4'):
			activeKey = '3'
		#result = 4
		elif (char == 'U' and activeKey == '8') or (char == 'R' and activeKey == '3'):
			activeKey = '4'	
		#result = 5
		elif (char == 'L' and activeKey == '6'):
			activeKey = '5'		
		#result = 6
		elif (char == 'D' and activeKey == '2') or (char == 'R' and activeKey == '5') or (char == 'L' and activeKey=='7') or (char == 'U' and activeKey=='A'):
			activeKey = '6'	
		#result = 7
		elif (char == 'D' and activeKey == '3') or (char == 'R' and activeKey == '6') or (char == 'L' and activeKey=='8') or (char == 'U' and activeKey=='B'):
			activeKey = '7'		
		#result = 8
		elif (char == 'D' and activeKey == '4') or (char == 'R' and activeKey == '7') or (char == 'L' and activeKey=='9') or (char == 'U' and activeKey=='C'):
			activeKey = '8'	
		#result = 9
		elif (char == 'R' and activeKey == '8'):
			activeKey = '9'
		#result = A
		elif (char == 'D' and activeKey == '6') or (char == 'L' and activeKey == 'B'):
			activeKey = 'A'
		#result = B
		elif (char == 'D' and activeKey == '7') or (char == 'R' and activeKey == 'A') or (char == 'L' and activeKey == 'C') or (char == 'U' and activeKey == 'D'):
			activeKey = 'B'
		#result = C
		elif (char == 'R' and activeKey == 'B') or (char == 'D' and activeKey == '8'):
			activeKey = 'C'
		#result = D
		elif (char == 'D' and activeKey == 'B'):
			activeKey = 'D'
	keyCode = keyCode + str(activeKey)
	
print ('Key code v2: %s') % keyCode
