from z3 import *
from  binascii import unhexlify
s=Solver()

r0,r1,r2,r3,r4,r5=0,0,0,0,0,0
X=BitVec('X',32)
Y=BitVec('Y',32)
r2=X
r3=Y

r0 =0x6F67202A
r0,r2 = r2,r0 #swap
r1=1

def hex1():
    global r0,r1,r2,r3,r4,r5
    r5 =0xA5D2F34
    r0=(r0+r5)&0xffffffff
    r0=r0^0xffffffff

hex1()

r2=(r2^r0)
r0 = 0x656C676F
r0,r3 = r3,r0
r1=6

def hex2():
    global r0,r1,r2,r3,r4,r5
    r0=r0^0xffffffff
    r5 = 0x48268673
    r0=(r0^r5)&0xffffffff

hex2()

r3=(r3^r0)&0xffffffff
r0 =0x6E696220
r1=0xf

def hex3():
    global r0,r1,r2,r3,r4,r5
    r5 = 0x5A921187
    r0=(r0^r5)&0xffffffff
    r5 = 0x100000000-0x1644E844
    r0=(r0+r5)&0xffffffff

hex3()
r0=(r0^r3)&0xffffffff
r2,r3 = r3,(r2^r0)&0xffffffff
r0 =0x682D616A
r1=0x1c

def hex4():
    global r0,r1,r2,r3,r4,r5
    r0=r0^0xffffffff
    r5 =0x100000000-0x28EFC82F
    r0=(r0^r5)&0xffffffff

hex4()

r0=(r0^r3)&0xffffffff
r2,r3= r3,r2^r0
r0 =0x67617865
r1=0x2d

def hex5():
    global r0,r1,r2,r3,r4,r5
    r0=r0^0xffffffff
    r5 =0x101FBCCC
    r0=(r0+r5)&0xffffffff

hex5()

r0=(r0^r3)&0xffffffff
r2,r3=r3, r2^r0
r0 = 0x2A206E6F
r1=0x42

def hex6():
    global r0,r1,r2,r3,r4,r5
    r5 = 0x100000000-0x74FE9C3F
    r0=(r0^r5)&0xffffffff
    r5 = 0x100000000-0x1131CD75
    r0=(r0^r5)&0xffffffff

hex6()

r0=(r0^r3)&0xffffffff
r2,r3=r3, r2^r0

s.add(r3==0x9D450E3D)
s.add(r2==0x6D80BF97)


print(s.check())
if s.check() == sat:
    m=s.model()
    x=m[X].as_long()
    y=m[Y].as_long()
    print(unhexlify(hex(x)[2:])[::-1]+unhexlify(hex(y)[2:])[::-1])

    




