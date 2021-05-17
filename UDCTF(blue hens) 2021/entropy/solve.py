from z3 import *

def enc(inp):
	return (0x5DEECE66D * inp +11) & 0xFFFFFFFFFFFF
	
s=Solver()
x=BitVec('x', 8*10)

for i in range(100):
	x=enc(x)
s.add(x==0xFD94E6E84A0A)


print(s.check())
print(s.model())