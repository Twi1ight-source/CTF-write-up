from z3 import *

s = Solver()

c1 = 31018867225649183750977872687351002051600286721243490293006893720934187569827

c2 = 95000751626272728732540896924058463535582995596703552905478832713420442258465

w1 = BitVec('w1', 256)
w2 = BitVec('w2', 256)
w3 = BitVec('w3', 256)
w4 = BitVec('w4', 256)
w5 = BitVec('w5', 256)
w6 = BitVec('w6', 256)
w7 = BitVec('w7', 256)
w8 = BitVec('w8', 256)
flag = BitVec('flag', 256)

s.add(0 == ~(w7 | w8))
s.add(w8 == ~(c2 | w6))
s.add(w7 == ~(w5 | w6))
s.add(w6 == ~(w5 | c2))
s.add(w5 == ~(w4 | w4))
s.add(w4 == ~(w2 | w3))
s.add(w3 == ~(c1 | w1))
s.add(w2 == ~(flag | w1))
s.add(w1 == ~(flag | c1))

print(s.check())
if s.check()==sat:
  print(s.model())
