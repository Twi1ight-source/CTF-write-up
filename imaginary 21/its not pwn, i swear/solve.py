from z3 import *
s=Solver()
a1=BitVec('a1',64)
a2=BitVec('a2',64)

s.add(((a1*0x6231726435333364)+a2)&0xffffffffffffffff ==0x317EE37C444051C9 )
s.add(((a1*0x317EE37C444051C9)+a2)&0xffffffffffffffff ==0x65bbfa1e87aa1f8d )

print(s.check())
if s.check()==sat:
    print(s.model())