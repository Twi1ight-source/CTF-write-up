from z3 import *
s=Solver()

inp=[BitVec(f'inp{i}',16) for i in range(32)]

def ASM_1795(a1,a2,a3):
    s.add(((a1 + a2) / 2) == (a3 + 32))

def ASM_1532(a1,a2):
    return (a1 >> 8 - a2 | (a1 << a2)) & 255


s.add(inp[0]==71)
s.add(inp[1]==70)
s.add(inp[2]==36)
s.add(inp[3]==56)
s.add(inp[31]==82)

ASM_1795(inp[2889-2880],inp[2907-2880],inp[2881-2880])
ASM_1795(inp[2894-2880],inp[2898-2880],inp[2911-2880])

s.add(inp[2889-2880]- inp[2898-2880] == -12)
s.add(inp[2907-2880]+ inp[2894-2880] ==216)

s.add(ASM_1532(inp[2908 - 2880],5) == 233)
s.add(ASM_1532(inp[2895 - 2880],3) == 178)
s.add(ASM_1532(inp[2890 - 2880],7) == 155)


s.add(inp[8] -inp[7] == 9)
s.add(inp[7] -inp[6] == 54)
s.add(inp[6] -inp[5] == 19)
s.add(inp[5] -inp[4] == -41)
s.add(inp[4] -inp[3] == 18)

s.add(inp[11]==ord('9'))
s.add(inp[12]==ord('O'))
s.add(inp[13]==ord('n'))

s.add((inp[2896-2880] & inp[2897-2880]) ==53)
s.add((inp[2897-2880] - inp[2909-2880]) ==-15)
s.add((inp[2909-2880] | inp[2910-2880]) ==116)
s.add((inp[2910-2880] + inp[2896-2880]) ==107)

s.add((inp[19] ^ (222&0xff)) +1 ==184&0xff)
s.add((inp[20] ^ (173&0xff)) +1 ==233&0xff) 
s.add((inp[21] ^ (190&0xff)) +1 ==156&0xff) 
s.add((inp[22] ^ (239&0xff)) +1 ==156&0xff) 
s.add((inp[23] ^ (222&0xff)) +1 ==150&0xff) 
s.add((inp[24] ^ (173&0xff)) +1 ==207&0xff) 
s.add((inp[25] ^ (190&0xff)) +1 ==235&0xff) 
s.add((inp[26] ^ (239&0xff)) +1 ==224&0xff) 

sat=s.check()
if str(sat)=='sat':
    model=s.model()
    for i in inp:
        c=model[i].as_long()
        print(chr(c),end="")
else:
    print(sat)