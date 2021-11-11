def enc(x,y,res,a3):
    rcx=res>>0x10
    r9=1
    r9+=a3
    r9+=x
    rcx+=r9
    r9+=y
    rcx+=r9

    rax=rcx
    rax=rax>>1
    rax+=0
    rax=rax>>0xf
    rax*=0xfff1
    rcx-=rax
    rax=rcx
    rax=rax<<0x10
    rax=rax|r9
    return rax

check=[0,0x14400D3, 0x42401aa,0x8bf028b,0xefa034f, 0x16a1040d, 0x200004ea,0x2ae20597, 0x3721065c, 0x4507072b,0x542f07cd, 0x651208a2, 0x77860970, 0x8b8f0a34, 0xa0d50adf, 0xb75c0b75, 0xcfa40c5e, 0xe9440d01, 0x4520db2,0x20b10e6e]
flag=[]
a3=0
from z3 import *
for j in range(len(check)):
    if j==19:
        break
    inp=[BitVec(f'{i}',32) for i in range(2)]
    s=Solver()
    for c in inp:
        s.add(c>0x20,c<0x7f)
    s.add(enc(inp[0],inp[1],check[j],a3)==check[j+1])

    if s.check() == sat:
        m=s.model()
        for i in inp:
            flag.append(m[i].as_long())
            a3+=m[i].as_long()

print(bytearray(flag).decode())