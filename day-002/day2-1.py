#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:18:03 2018

@author: switt
"""

# Advent of Code Day 2

filename = "input-day2.txt"

boxInput = [line.strip('\n') for line in open(filename)]

#Part 1

boxList = []
boxList2 = []
boxList3 = []

dict = {}
dictTemp = {}
dictTemp2 = {}
dictTemp3 = {}
    
for b in range(len(boxInput)):
    for letter in boxInput[b]:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    dictTemp[b] = dict    
    dictTemp2[b] = {k:v for k, v in dictTemp[b].items() if v == 2}
    dictTemp3[b] = {k:v for k, v in dictTemp[b].items() if v == 3}
    dict = {} 
    if len(dictTemp2[b]) != 0:
        boxList2.append(boxInput[b])
    if len(dictTemp3[b]) != 0:
        boxList3.append(boxInput[b])
            
checksum = len(boxList2) * len(boxList3)
print('Checksum = {:d}'.format(checksum))

#Part 2

diff = []

def difference(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

for a in range(len(boxInput)):
    for b in range(len(boxInput)):
        bA = boxInput[a]
        bB = boxInput[b]
        diff = difference(bA,bB)
        if diff == 1:
            box1 = boxInput[a]
            box2 = boxInput[b]
            for d in range(len(box1)):
                if box1[d] != box2[d]:
                    remove = d
                  
print('Box 1 ID: {:s}'.format(box1))
print('Box 2 ID: {:s}'.format(box2))
print('Unique ID character: {:s}'.format(box2[remove]))
print('Common ID characters: {:s}'.format(box1[0:remove] + box1[remove+1:len(box1)]))

        

    
        
    


            



            
    