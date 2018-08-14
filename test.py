#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:16:27 2018

@author: matthew.mu
"""

from hdb import HDB

i = int('111111'*10, 2)
j = int('011111'*10, 2)

hdb = HDB(i, j)

print(hdb.hamming_distance_1())
print(hdb.hamming_distance_2())
print(hdb.hamming_distance_3())
print(hdb.hamming_distance_32bit())
print(hdb.hamming_distance_64bit())
