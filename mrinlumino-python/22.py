#!/usr/bin/python
# -*- coding: utf-8 -*-


print ''
print '***************************************************************************************'
print '*                                                                                     *'
print '*                              Advent of code 2016 22/12                               *'
print '*                             @MrInlumino - Anders Rosen                              *'
print '*                                                                                     *'
print '***************************************************************************************'
print ''


# ****************************************** challenge 1 ****************************************** 
print '********** Challenge 1 ************'


# Open input data file and read it into a string
data=[]
fo = open('22.data','r')
for line in fo:
    if line[0] == '/':
        data.append(line.replace('\n','').replace('    ',' ').replace('   ',' ').replace('  ',' ').replace('T','').split(' '))
fo.close()

dataCopy = data
noOfPairs = 0

# Loop over all lines in the first set
for line in data:
    # For each line in the first set, loop over each line in the copy and look for pairs
    for line2 in dataCopy:
        # Check the criterias
        if line[2] != '0' and line[0] != line2[0] and int(line[2]) <= int(line2[3]):
            # If the criterias as met, increase the counter of pairs
            noOfPairs += 1

print 'Challenge 1: Number of valid pairs are %s' % noOfPairs