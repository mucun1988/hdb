#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:21:09 2018

@author: matthew.mu
"""
from bitstring import Bits

class HDB(object):
    
    def __init__(self, x, y, nb=32):
        self.x = x
        self.y = y
        assert nb in [32, 64], "only supports number of bits to be either 32 or 64"
        self.nb = nb
        
    # def hamming_distance_1(self):
    #     distance = 0
    #     z = self.x ^ self.y
    #     while z:
    #         distance += 1
    #         z &= z - 1
    #     return distance

    def hamming_distance(self):
        return Bits(int=self.x ^ self.y, length=self.nb).count('1')


    def hamming_distance_bm(self):

        if self.nb == 32:
            return self._hamming_distance_32bit()
        elif self.nb == 64:
            return self._hamming_distance_64bit()

    
    def _hamming_distance_32bit(self):
        """
        https://blogs.msdn.microsoft.com/jeuge/2005/06/08/bit-fiddling-3/
        3681400539: Bits(oct='0o33333333333').int
        1227133513: Bits(oct='11111111111').int
        3340530119: Bits(oct='30707070707').int

        -613566757 = Bits(bin='11011011011011011011011011011011').int
        1227133513 = Bits(bin='01001001001001001001001001001001').int
        -954437177 = Bits(bin='11000111000111000111000111000111').int
        """
        # u = self.x ^ self.y
        # uCount = u - ((u >> 1) & 3681400539) - ((u >> 2) & 1227133513)
        # return ((uCount + (uCount >> 3)) & 3340530119) % 63
        u = self.x ^ self.y
        uCount = u - ((u >> 1) & -613566757) - ((u >> 2) & 1227133513)
        return ((uCount + (uCount >> 3)) & -954437177) % 63
    
    def _hamming_distance_64bit(self):
        """
        13176245766935394011: int('1011011011011011011011011011011011011011011011011011011011011011',2)
        10540996613548315209: int('1001001001001001001001001001001001001001001001001001001001001001',2)
        8198552921648689607:  int('0111000111000111000111000111000111000111000111000111000111000111',2)

        -5270498306774157605: Bits(bin='1011011011011011011011011011011011011011011011011011011011011011').int
        -7905747460161236407: Bits(bin='1001001001001001001001001001001001001001001001001001001001001001').int
        8198552921648689607: Bits(bin='1001001001001001001001001001001001001001001001001001001001001001').int
        """
        # u = self.x ^ self.y
        # uCount = u - ((u >> 1) & 13176245766935394011) - ((u >> 2) & 10540996613548315209)
        # return ((uCount + (uCount >> 3)) & 8198552921648689607) % 63

        u = self.x ^ self.y
        uCount = u - ((u >> 1) & -5270498306774157605) - ((u >> 2) & -7905747460161236407)
        return ((uCount + (uCount >> 3)) & 8198552921648689607) % 63

