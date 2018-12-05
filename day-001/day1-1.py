#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:31:14 2018

@author: switt
"""
# Advent of Code Day 1

freqOrig = 0

filename = "input-day1.txt"

freqCalib = sum([int(line.strip('\n')) for line in open(filename)])
print('Day 1 Part 1: the frequency is {:d}'.format(freqCalib)) 



freq = 0
freqFound = set()
i = 0

freqInput = [int(line.strip('\n')) for line in open(filename)]

while ((freq in freqFound) == False):
    freqFound.add(freq)
    freq = freq + freqInput[i]
    i = (i + 1) % len(freqInput)
print('Day 1 Part 2: The first duplicate frequency is {:d}'.format(freq))


    






