#!/usr/bin/python
# -*- coding: utf-8 -*-

# Advent of code 2016 4/12

# Open input data file and read it into a string
data=[]

fo = open('indata.txt','r')
for line in fo:
	line = line.replace('\n','').strip(' ')
	checksum = line[line.rfind('['):].strip('[').strip(']')
	lineWihtoutChecksum = line[0:line.rfind('[')]
	sectorID = int(lineWihtoutChecksum[lineWihtoutChecksum.rfind('-')+1:])
	ecnryptedName=lineWihtoutChecksum[0:lineWihtoutChecksum.rfind('-')]
	#print ('%s : Name: %s | Checksum: %s | SectorID: %s') % (line, ecnryptedName, checksum, sectorID)
	#print ecnryptedName
	data.append([ecnryptedName,sectorID, checksum])
	#lines.append(line.replace('\n','').strip(' '))
fo.close()

sumOfSectorID = 0


for room in data:
	name=room[0].replace('-','')
	nameWithDashes = room[0]
	sectorID = room[1]
	checksum = room[2]
	checkSumOK = 1
	decodedName = ''
	for n in range(5):
		#create a sorted list of character from the name
		namelist = sorted(name)
		
		#find the most common character
		checksumChar = max(namelist,key=namelist.count)
		#print ('%s:%s:%s') % (name, checksumChar,checksum[n])
		
		#strip the first character from the name
		name = name.replace(checksumChar,'')
		
		#compare the identified character to the corresponding checksum character
		if checksumChar != checksum[n]: 
			checkSumOK = 0
	

	for decodingChar in nameWithDashes:
		if decodingChar == '-': 
			decodedName += ' '
		else:
			for sectorCount in range(sectorID):
				if decodingChar == 'z': 
					decodingChar = 'a'
				else:
					decodingChar = chr(ord(decodingChar)+1)
			decodedName += decodingChar

	if checkSumOK == 1:
		sumOfSectorID += sectorID
		print ('Decoded name: %s | Original name: %s | Checksum: %s | SectorID: %s | Cheksum OK: %s') % (decodedName, nameWithDashes, checksum, sectorID, checkSumOK)


print ('Sum of sectorID:s for correct room is: %s') % sumOfSectorID