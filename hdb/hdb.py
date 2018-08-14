#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:21:09 2018

@author: matthew.mu
"""

# Time:  O(1)
# Space: O(1)

# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#       ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

class HDB(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def hamming_distance_1(self):
        distance = 0
        z = self.x ^ self.y
        while z:
            distance += 1
            z &= z - 1
        return distance

    def hamming_distance_2(self):
        return bin(self.x ^ self.y).count('1')
    
    
    def hamming_distance_3(self):
        z = self.x ^ self.y
        dist = 0
        while z:
            dist += z & 1
            z >>= 1
        return dist

    
    def hamming_distance_32bit(self):
        """
        https://blogs.msdn.microsoft.com/jeuge/2005/06/08/bit-fiddling-3/
        """
        u = self.x ^ self.y
        uCount = u - ((u >> 1) & 3681400539) - ((u >> 2) & 1227133513)
        return ((uCount + (uCount >> 3)) & 3340530119) % 63
    
    def hamming_distance_64bit(self):
        """
        13176245766935394011: int('1011011011011011011011011011011011011011011011011011011011011011',2)
        10540996613548315209: int('1001001001001001001001001001001001001001001001001001001001001001',2)
        8198552921648689607:  int('0111000111000111000111000111000111000111000111000111000111000111',2)
        """
        u = self.x ^ self.y
        uCount = u - ((u >> 1) & 13176245766935394011) - ((u >> 2) & 10540996613548315209)
        return ((uCount + (uCount >> 3)) & 8198552921648689607) % 63
    
    
    
    
              
              
              
