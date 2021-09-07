target="inctf{U_Sur3_m4Te?}"

from z3 import *
s=Solver()

inp=[BitVec(f'{i}',32) for i in range(30)]

for i in range(len(inp)):
    s.add(inp[i]>0x20)
    s.add(inp[i]<0x7f)
    
x1=[0]*22
x2=[0]*22

x1[0]=inp[0]-50 + inp[1]
x1[1]=inp[1] -100 + inp[2]
x1[2]=4*inp[2]
x1[3]=inp[3] ^ 0x46
x1[4]=36 -(inp[3]- inp[4])

x1[6]=inp[6]*inp[5] +99
x1[7]=inp[6] ^ inp[7]
x1[8]=(inp[7]+45) ^inp[8]
x1[9]= (inp[9] & 0x37) - 3

x1[11]=inp[11]- 38
x1[12]=4 *((inp[12] ^ inp[6]) +4)

x1[5]=(inp[21]- inp[4]) ^ 0x30

x1[13]=inp[13]-inp[14]-1
x1[10]=inp[17]- inp[16] +82
x1[16]= 6*(inp[18]+ inp[19]) +54
x1[17]= inp[21]+49 +(inp[20] ^0x73)
x1[14]=inp[22]
x1[18]=inp[23] ^0x42
x1[15]=inp[26]+5
x1[19]= inp[25] - (inp[26] / 2) - 55
x1[20]=4 * inp[27] - (inp[28] + 128)
x1[21]=inp[29]- 32

x2[0]= ((x1[0] ^2) -31)&0xff
x2[1]=(((x1[1] % 2) ^ x1[0]) - 29)&0xff
x2[2]=((4 * x1[1]) ^ 0x97)&0xff
x2[3]=(x1[2] ^ 0xA0)&0xff
x2[4]=((x1[3] ^ 0x4D) + 7)&0xff
x2[5]=(4 * x1[5] - 1)&0xff
x2[3]=(x1[4] + 116)&0xff
x2[6]=(x1[6] + 21)&0xff
x2[7]=(x1[7] - 20)&0xff
x2[8]=(x1[8] ^ 0x63)&0xff
x2[9]=((x1[10] ^ 3) - x1[8] + 54)&0xff
x2[10]=(x1[9] ^ 0x42)&0xff
x2[11]=(x1[11] + 51)&0xff
x2[11]=(x1[12] ^ 0xB3)&0xff
x2[12]=((x1[13] + 18) ^ 0x1A)&0xff
x2[13]=(x1[14] - 7)&0xff
x2[14]=(x1[15] - 37)&0xff
x2[15]=(x1[17] ^ 0xE5)&0xff
x2[16]=((x1[18] & 0x36) + 53)&0xff
x2[14]=(x1[19] ^ 0x34)&0xff
x2[17]=(x1[20] ^ 0xFD)&0xff
x2[18]=((x1[20] >> x1[21]) ^ 0x1C)&0xff

for i in range(len(target)):
    s.add(x2[i]== ord(target[i]))

print(s.check())
w=""
if s.check() == sat:
    m=s.model()
    for i in range(len(inp)):
        w+=chr(m[inp[i]].as_long())
print(w)
    