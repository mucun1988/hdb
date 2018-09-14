#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:16:27 2018

@author: matthew.mu
"""

from bitstring import Bits
import random
from hdb import HDB
from bitstring import BitArray, BitStream

for xx in range(100000):
    i = Bits(uint=random.getrandbits(64), length=64).int
    j = Bits(uint=random.getrandbits(64), length=64).int
    hdb = HDB(i, j, 64)
    d1 = hdb.hamming_distance()
    d2 = hdb.hamming_distance_bm()
    assert d1 == d2

# not working yet
for i in range(1000000):
    i = Bits(uint=random.getrandbits(32), length=32).int
    j = Bits(uint=random.getrandbits(32), length=32).int
    hdb = HDB(i, j, 32)
    d1 = hdb.hamming_distance()
    d2 = hdb.hamming_distance_bm()
    assert d1 == d2

