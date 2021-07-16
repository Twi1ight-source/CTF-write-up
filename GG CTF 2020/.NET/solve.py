from z3 import *
s=Solver()

def xor(inp):
    array=[0x1F, 0x23, 0x3F, 0x3F, 0x1B, 0x7, 0x37, 0x21,  0x4, 0x33, 0x9, 0x3B, 0x39, 0x28, 0x30, 0xC,
0xE, 0x2E, 0x3F, 0x25, 0x2A, 0x27, 0x3E, 0xB, 0x27, 0x1C, 0x38, 0x31, 0x1E, 0x3D]
    result=[]
    for i in range(30):
        result.append(inp[i] ^ array[i])
    return result

def checksum(inp):
    num =16
    for i in range(len(inp)):
        if i!=len(inp)-2:
            num=inp[i]+num
            if i%2==0:
               num=inp[i]+num
            if i%3 ==0:
                num = inp[i] * 4294967294 + num
            if i%5==0:
                num = inp[i] * 4294967293 + num
            if i%7==0:
                num = inp[i] * 4 + num

            
    return num&63

def random_shuffle(inp):
    random_num = [0, 1, 0, 2, 3, 3, 7, 0, 6, 7, 7, 0, 3, 0xa, 0x6, 0xf, 0x3, 0x5, 0xc, 0xe, 0x3, 0x5, 0x8, 0x11, 0x17, 0x16, 0xa]
    i=1
    for j in random_num:
        if j !=i:
            tmp=inp[i]
            inp[i]=inp[j]
            inp[j]=tmp
        i+=1
    return inp

def swap_more(inp):
    for i in range(0,len(inp)-3,3):
        if i!=28 and i !=29:
            tmp=inp[i]
            inp[i]=inp[i+1]
            inp[i+1]=tmp
    return inp

def final(MATHOPEN):
    s.add(MATHOPEN[1] == 25)
    s.add(MATHOPEN[2] == 23)
    s.add(MATHOPEN[9] == 9)
    s.add(MATHOPEN[20] == 45)
    s.add(MATHOPEN[26] == 7)
    s.add(UGE(MATHOPEN[8], 15))
    s.add(ULE(MATHOPEN[12], 4))
    s.add(UGE(MATHOPEN[14], 48))
    s.add(UGE(MATHOPEN[29], 1))

    s.add(ULE(MATHOPEN[0] + MATHOPEN[1] + MATHOPEN[2] + MATHOPEN[3] + MATHOPEN[4] - 130, 10))
    s.add(ULE(MATHOPEN[5] + MATHOPEN[6] + MATHOPEN[7] + MATHOPEN[8] + MATHOPEN[9] - 140, 10))
    s.add(ULE(MATHOPEN[10] + MATHOPEN[11] + MATHOPEN[12] + MATHOPEN[13] + MATHOPEN[14] - 150 ,10)) 
    s.add(ULE(MATHOPEN[15] + MATHOPEN[16] + MATHOPEN[17] + MATHOPEN[18] + MATHOPEN[19] - 160 ,10)) 
    s.add(ULE(MATHOPEN[20] + MATHOPEN[21] + MATHOPEN[22] + MATHOPEN[23] + MATHOPEN[24] - 170 ,10)) 

    s.add(ULE(MATHOPEN[0] + MATHOPEN[5] + MATHOPEN[10] + MATHOPEN[15] + MATHOPEN[20] + MATHOPEN[25] - 172, 6)) 
    s.add(ULE(MATHOPEN[1] + MATHOPEN[6] + MATHOPEN[11] + MATHOPEN[16] +MATHOPEN[21] + MATHOPEN[26] - 162, 6)) 
    s.add(ULE(MATHOPEN[2] + MATHOPEN[7] + MATHOPEN[12] + MATHOPEN[17]+ MATHOPEN[22] + MATHOPEN[27] - 152, 6)) 
    s.add(ULE(MATHOPEN[3] + MATHOPEN[8] + MATHOPEN[13] + MATHOPEN[18] + MATHOPEN[23] - 142, 6)) 
    s.add(ULE(MATHOPEN[4] + MATHOPEN[9] + MATHOPEN[14] + MATHOPEN[19] + MATHOPEN[24] + MATHOPEN[29] - 132, 6)) 

    num45 = ((MATHOPEN[7] + (MATHOPEN[27] * 3)) * 3 - MATHOPEN[5] * 13) - 57
    s.add(ULE(num45, 28))
  
    num45 = (MATHOPEN[22] * 3 + ((MATHOPEN[14] << 2) - (MATHOPEN[20] * 5))) - 12
    s.add(ULE(num45, 70))

    num46 = (MATHOPEN[14] + (MATHOPEN[16] * 2)) * 2 + ((MATHOPEN[15] - ( MATHOPEN[18] * 2)) * 3) - MATHOPEN[17] * 5
    s.add(MATHOPEN[13] + num46 == 0)

    s.add(MATHOPEN[5] == MATHOPEN[6] * 2)
    s.add(MATHOPEN[29] + MATHOPEN[7] == 59)
    s.add(MATHOPEN[0] == MATHOPEN[17] * 6)
    s.add(MATHOPEN[8] == MATHOPEN[9] * 4)
    s.add(MATHOPEN[11] << 1 == MATHOPEN[13] * 3)
    s.add(MATHOPEN[13] + MATHOPEN[29] + MATHOPEN[11] + MATHOPEN[4] == MATHOPEN[19])
    s.add(MATHOPEN[10] == MATHOPEN[12] * 13)


inp=[]
for i in range(30):
    b = BitVec("%d_i" % i, 32)
    inp.append(b)
    s.add(ULE(inp[i], 63))

xor_ret=xor(inp)
res=random_shuffle(xor_ret)
res1=swap_more(res)

s.add(Distinct(res1))
ret_checksum=checksum(res1)
s.add(res1[28]==ret_checksum)
final(res1)

print(s.check())
if s.check()==sat:
    model=s.model()
    for i in inp:
        c=model[i].as_long()
        print(c,end=",")



