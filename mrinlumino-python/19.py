#!/usr/bin/python
# -*- coding: utf-8 -*-


print ''
print '***************************************************************************************'
print '*                                                                                     *'
print '*                              Advent of code 2016 19/12                               *'
print '*                             @MrInlumino - Anders Rosen                              *'
print '*                                                                                     *'
print '***************************************************************************************'
print ''




# # ****************************************** challenge 1 ****************************************** 
# print '********** Challenge 1 ************'

# NoOfElves = 3005290


# # Create an array corresponding to the elves with one present each
# elves = []
# for createCounter in range(NoOfElves): elves.append(createCounter+1)


# elfCounter = 0
# # Do the present shift and exclusion of elves until there is only one elf left
# while len(elves) > 1:
# 	if len(elves) % 10000 == 0: print len(elves) / 10000

# 	# Are we currently at the last elf in the ring, then remove the first one, otherwise just remove the next in line
# 	if elfCounter == len(elves)-1:
# 		elves.pop(0)
# 	else:
# 		elves.pop(elfCounter+1)

# 	elfCounter += 1
# 	if elfCounter >= len(elves): elfCounter = 0

# print 'The last remaining elf with presents is: %s' % elves




# ****************************************** challenge 2 ****************************************** 
print '********** Challenge 2 ************'

NoOfElves = 3005290


# Create an array corresponding to the elves with one present each
elves = []
for createCounter in range(NoOfElves): elves.append(createCounter+1)

#print elves
elfCounter = 0
# Do the present shift and exclusion of elves until there is only one elf left
while len(elves) > 1:
	if len(elves) % 10000 == 0: print len(elves) / 10000

	# Calclulate the elf to be removed
	removeElfNo = len(elves)//2 + 1 + elfCounter
	if removeElfNo > len(elves)-1: removeElfNo -= len(elves)

	#Remove the elf
	elves.pop(removeElfNo)

	#print elves
	elfCounter += 1
	if elfCounter >= len(elves): elfCounter = 0

print 'The last remaining elf with presents is: %s' % elves