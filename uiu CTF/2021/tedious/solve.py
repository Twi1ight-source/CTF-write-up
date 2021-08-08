from z3 import *
S=Solver()

s=[BitVec(f'{i}',8) for i in range(39)]

for i in range(39):
    s[i]=(s[i] + 59) ^ 0x38

for i in range(39):
    s[i] = (s[i] + 18) ^ 0xFD

for i in range(39):
    s[i] = (s[i] + 4) ^ 0x50

for i in range(39):
    s[i] = (s[i] + 19) ^ 0x68

for i in range(39):
    s[i] = (s[i] + 12) ^ 0x79

for i in range(39):
    s[i] = (s[i] - 68) ^ 0xA0

for i in range(39):
    s[i] = (s[i] + 10) ^ 0xCD

for i in range(39):
    s[i] = (s[i] - 72) ^ 0x5A

for i in range(39):
    s[i] = (s[i] + 11) ^ 0xBD

for i in range(39):
    s[i] = (s[i] - 31) ^ 0xED

for i in range(39):
    s[i] = (s[i] + 69) ^ 0x22

for i in range(39):
    s[i] = (s[i] - 66) ^ 0x6B

for i in range(39):
    s[i] = (s[i] - 38) ^ 0x6B

for i in range(39):
    s[i] = (s[i] + 118) ^ 0xFA

for i in range(39):
    s[i] = (s[i] + 22) ^ 0x6B

for i in range(39):
    s[i] = (s[i] - 75) ^ 0x6B

for i in range(39):
    s[i] = (s[i] - 115) ^ 0x64

for i in range(39):
    s[i] = (s[i] + 10) ^ 0xAB

for i in range(39):
    s[i] = (s[i] + 99) ^ 0x1B

for i in range(39):
    s[i] = (s[i] - 43) ^ 0xF0

for i in range(39):
    s[i] = (s[i] + 117) ^ 0x6B

check=[77,185,77,11,212,102,227,41,184,77,223,102,184,77,14,196,223,212,20,59,223,102,44,20,71,223,183,184,183,223,71,77,164,223,50,184,234,245,146]

for i in range(39):
    S.add(s[i]==check[i])

print(S.check())
flag=""
if S.check() ==sat:
    m=S.model()
    print(m)




