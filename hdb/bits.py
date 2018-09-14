from bitstring import BitArray, BitStream


a = BitArray('0xff01')
b = BitArray('0b110')

print(a)
print(b)

print(a.bin)
print(b.oct)

c = Bits(bin='0b110')
print(c.int)
print(b.int)


c = Bits(bin='0b'+'1'*64)