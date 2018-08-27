#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:16:27 2018

@author: matthew.mu
"""

import random
from hdb import HDB

for i in range(1000000):
    i = random.getrandbits(64)
    j = random.getrandbits(64)
    hdb = HDB(i, j)
    d1 = hdb.hamming_distance_1()
    d2 = hdb.hamming_distance_64bit()
    assert d1 == d2

for i in range(1000000):
    i = random.getrandbits(32)
    j = random.getrandbits(32)
    hdb = HDB(i, j)
    d1 = hdb.hamming_distance_1()
    d2 = hdb.hamming_distance_32bit()
    assert d1 == d2
