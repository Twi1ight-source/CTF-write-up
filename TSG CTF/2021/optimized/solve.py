from z3 import *
s=Solver()

inp=BitVec('inp',128)
inp1=BitVec('inp1',128)
inp2=BitVec('inp2',128)
inp3=BitVec('inp3',128)

s.add(inp>0, inp<0xffffffff)
s.add(inp1>0, inp1<0xffffffff)
s.add(inp2>0, inp2<0xffffffff)
s.add(inp3>0, inp3<0xffffffff)

s.add( LShR((((inp*0x5F50DDCA7B17)&0xffffffffffffffff) *0x2AF91),64) &0x3FFFF  == 0x9569 )
s.add( LShR((((inp*0x4DC4591DAC8F)&0xffffffffffffffff) *0x34AB9),64) &0x3FFFF  == 0x26CF2 )

s.add( LShR((((inp1*0x4AE11552DF1A)&0xffffffffffffffff) *0x36B39),64) &0x3FFFF  == 0x20468 )
s.add( LShR((((inp1*0x46680B140EFF)&0xffffffffffffffff) *0x3A2D3),64) &0x3FFFF  == 0x3787A )

s.add((inp2*0x4D935BBD3E0)&0xffffffffffffffff <0x4D935BBD3E0)
s.add( LShR((((inp2*0x66B9B431B9ED)&0xffffffffffffffff) *0x27DF9),64) &0x3FFFF  == 0x5563 )

s.add((inp3*0x1E5D2BE81C5)&0xffffffffffffffff <0x1E5D2BE81C5)
s.add( LShR((((inp3*0x448626500938)&0xffffffffffffffff) *0x3BC65),64) &0x3FFFF  == 0x133E7 )

if s.check() == sat:
    m=s.model()
    print(m)

