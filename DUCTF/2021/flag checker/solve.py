from z3 import *
s = Solver()

def sub_17C3(a1):
    return ((2 * a1) ^ (27 * LShR(a1,7)))


def trans(a1,a2):
    v9 = a1[a2[0]] 
    v10 =a1[a2[1]] 
    v11 =a1[a2[2]] 
    v12 =a1[a2[3]] 
    v13 =a1[a2[4]] 
    v14 =a1[a2[5]] 

    v2 = v11 ^ v9 ^ sub_17C3(v9)
    v3 = sub_17C3(v11) ^ v2
    v15 = v3 ^ sub_17C3(v13)
    v4 = v12 ^ v10 ^ sub_17C3(v10)
    v5 = sub_17C3(v12) ^ v4
    v16 = v5 ^ sub_17C3(v14)
    v17 = v13 ^ sub_17C3(v9)
    v18 = v14 ^ sub_17C3(v10)
    v6 = v9 ^ sub_17C3(v9)
    v19 = v6 ^ sub_17C3(v11)
    v7 = sub_17C3(v10)
    v20 = v10 ^ v7 ^ sub_17C3(v12)

    
    a1[a2[0]] =v15
    a1[a2[1]] =v16
    a1[a2[2]] =v17
    a1[a2[3]] =v18
    a1[a2[4]] =v19
    a1[a2[5]] =v20
    return a1

def enc_1(inp):
    v2=[0,1,2,6,12,18]
    v3=[3,4,5,11,17,23]
    v4=[7,8,9,13,14,15]
    v5=[10,16,22,28,29,35]
    v6=[19,20,24,25,26,30]
    v7=[21,27,31,32,33,34]

    inp=trans(inp,v2)
    inp=trans(inp,v3)
    inp=trans(inp,v4)
    inp=trans(inp,v5)
    inp=trans(inp,v6)
    inp=trans(inp,v7)
    return inp

shuffle_order=[23, 16, 19, 12, 31, 24, 17, 22, 13, 18, 25, 30, 9, 2, 11, 4, 33, 26, 3, 8, 5, 10, 27,
32, 21, 14, 35, 28, 7, 0, 15, 20, 29, 34, 1, 6]

arr=[15, 79, 115, 60, 65, 198, 164, 175, 180, 65, 214, 101, 200, 153, 170, 179,
       108, 153, 97, 60, 78, 221, 112, 70, 21, 102, 60, 27, 127, 22, 166, 111, 35, 19, 18, 110]

for i in range(16):
    new_arr=[0]*36
    for j in range(36):
        new_arr[shuffle_order[j]] = arr[j]

    s=Solver()
    inp=[BitVec(f'inp_{k}',8) for k in range(36)]
    a=enc_1(inp)

    for j in range(36):
        s.add(a[j]==new_arr[j])
    
    w=[]
    inp=[BitVec(f'inp_{k}',8) for k in range(36)]
    if s.check() == sat:
        m=s.model()
        for f in inp:
            w.append(m[f].as_long())
    arr=w

print(bytearray(w).decode())