from z3 import *
s=Solver()

inp=[BitVec(f'inp_{i}',32) for i in range(5)]

for i in range(5):
    v9 = 19753 * (i + 1)
    s.add(inp[i] < 1000000, inp[i]>0)
    s.add(inp[i] %v9 ==0)

print(s.check())
if s.check() ==sat:
    print(s.model())

