from z3 import *
s=Solver()

v15=open('yougotrickrolled1.bmp', 'rb').read()
v16=open('yougotrickrolled2.bmp', 'rb').read()
v17=open('yougotrickrolled3.bmp', 'rb').read()

inp=[BitVec(f'inp{i}',32) for i in range(50)]

def sub_1268(a1,a2,a3):
    return ((a3 >> a1) & 1) | (a2 & 0xFFFFFFFE)

l=[]
v5=[]
for i in range(4800,len(v15)):
    if v15[i]==v17[i]:
        l.append(v16[i])
        v5.append(v15[i])

    elif v15[i]==v16[i]:
        l.append(v17[i])
        v5.append(v15[i])
        
    elif v16[i]==v17[i]:
        l.append(v15[i])
        v5.append(v16[i])


g=0
for j in range(50):
    for k in range(8):
        s.add(sub_1268(k,v5[g],inp[j]^0x68) == l[g])
        g+=1

print(s.check())
if s.check() ==sat:
    m=s.model()
    for c in inp:
        print(chr(m[c].as_long()), end="")
        