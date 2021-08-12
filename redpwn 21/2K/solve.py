from z3 import *
import struct
s=Solver()

opc=open('prog.bin', 'rb').read()
flag=[BitVec(f'{i}',16) for i in range(64)]
pos=0

rip=0
stack=[]
mem=[0]*100
cx=0

while rip<len(opc):
    if opc[rip]==1:
        lastEl =stack[-1]
        stack.append(lastEl)
        rip+=1
    elif opc[rip]==2:
        stack.pop(-1)
        rip+=1
    elif opc[rip]==3:
        token=stack.pop()
        rip+=1
        break
    elif opc[rip]==0x10:
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b)
        rip+=1
    elif opc[rip]==0x11:
        a=stack.pop()
        b=stack.pop()
        stack.append(a-b)
        rip+=1
    elif opc[rip]==0x12:
        a=stack.pop()
        b=stack.pop()
        stack.append(a*b)
        rip+=1
    elif opc[rip]==0x13:
        a=stack.pop()
        b=stack.pop()
        stack.append(a/b)
        rip+=1
    elif opc[rip]==0x14:
        a=stack.pop()
        b=stack.pop()
        stack.append(a%b)
        rip+=1
    elif opc[rip]==0x15:
        a=stack.pop()
        b=stack.pop()
        c=stack.pop()
        stack.append((c*b)%a)
        rip+=1
    elif opc[rip]==0x16:
        a=stack.pop()
        b=stack.pop()
        stack.append(If(a==b, BitVecVal(1,16), BitVecVal(0,16)))
        rip+=1
    elif opc[rip]==0x17:
        a=stack.pop()
        stack.append(If(a==0, BitVecVal(0,16), If(a>0, BitVecVal(1,16), BitVecVal(-1,16))))
        rip+=1
    elif opc[rip]==0x20:
        stack.append(flag[pos])
        pos+=1
        rip+=1
    elif opc[rip]==0x21:
        print(chr(stack.pop()),end="")
        rip+=1
    elif opc[rip]==0x22:
        num=struct.unpack('<H', opc[rip+1:rip+3])[0]
        stack.append(num)
        rip+=3
    elif opc[rip]==0x30:
        addr=stack.pop()
        rip=abs(addr)
    elif opc[rip]==0x31:
        a=stack.pop()
        b=stack.pop()
        if a==4:
            s.add(b!=0)
            rip+=1
        else:
            rip+=1
    elif opc[rip]==0x32:
        a=stack.pop()
        b=stack.pop()
        if a==4:
            s.add(b==0)
            rip+=1
        else:
            rip+=1
    
    elif opc[rip]==0x33:
        a=stack.pop()
        b=stack.pop()
        if a==4:
            s.add(b>=0)
            rip+=1
        else:
            rip+=1
    elif opc[rip]==0x34:
        a=stack.pop()
        b=stack.pop()
        if a==4:
            s.add(b<=0)
            rip+=1
        else:
            rip+=1
    elif opc[rip]==0x35:
        a=stack.pop()
        b=stack.pop()
        if a==4:
            s.add(b>0)
            rip+=1
        else:
            rip+=1
    elif opc[rip]==0x36:
        a=stack.pop()
        b=stack.pop()
        if a==4:
            s.add(b<0)
            rip+=1
        else:
            rip+=1
    
    elif opc[rip]==0x40:
        a=stack.pop()
        mem[cx]=a
        rip+=1
    
    elif opc[rip]==0x41:
        stack.append(mem[cx])
        rip+=1
    elif opc[rip]==0x50:
        cx+=1
        rip+=1
    elif opc[rip]==0x51:
        cx-=1
        rip+=1
    elif opc[rip]==0x52:
        cx+=stack.pop()
        rip+=1
    elif opc[rip]==0x53:
        cx-=stack.pop()
        rip+=1
    else:
        print('ERROR')
        break

for c in flag:
    s.add(And(c>46, c<=127))

print(s.check())
if s.check()==sat:
    m=s.model()
    for k in flag:
        print(chr(m[k].as_long()),end="")  

    

