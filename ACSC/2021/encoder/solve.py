-----------------find random number-------------------
def enc(inp,rand,i):
    
    a=inp ^ rand

    b= a>>0xd

    c= a>>3
    c= (c ^ 0xffffffff) &0x1f

    d= (a^ 0xffffffff) &7

    e= c <<0xb
    e= e | (b<<8)
    e= e | (d<<5)

    h=(e >> (((i+1)*3) &0xf))&0xffffffff
        
    k= (e << (0x10 -(((i+1)*3) &0xf)))&0xffffffff

    res= (h | k)&0xffff
    return res

inp=[0xff, 0xd8, 0xff, 0xe0, 0x00,0x10, 0x4a,0x46]
target=[0xa00,0x81c3,0x28,0x8e04,0x51c1,0x2e38,0x705,0x20e8]
for i in range(len(inp)):
    for random in range(0xff+1):
        if enc(inp[i],random,i) == target[i]:
            print(random,end=",")
            break

---->correct random =80

------------------------------Solve------------------------------------------


def enc(inp,rand,i):
    
    a=inp ^ rand

    b= a>>0xd

    c= a>>3
    c= (c ^ 0xffffffff) &0x1f

    d= (a^ 0xffffffff) &7

    e= c <<0xb
    e= e | (b<<8)
    e= e | (d<<5)

    h=(e >> (((i+1)*3) &0xf))&0xffffffff
        
    k= (e << (0x10 -(((i+1)*3) &0xf)))&0xffffffff

    res= (h | k)&0xffff
    return res


f=open('flag.jpg.enc', 'rb').read()
arr=[]
for i in range(len(f)):
    arr.append(hex(f[i]))
arr1=[]
for j in range(0, len(arr), 2):
    if len(arr[j]) ==4 and len(arr[j+1]) ==4:
        arr1.append(f'0x{arr[j+1][2:]}{arr[j][2:]}')
    else:
        if len(arr[j]) == 3:
            arr[j]= f'0x0{arr[j][-1]}'
        if len(arr[j+1]) == 3:
            arr[j+1]= f'0x0{arr[j+1][-1]}'
        arr1.append(f'0x{arr[j+1][2:]}{arr[j][2:]}')
arr2=[]
for m in arr1:
    arr2.append(int(m,16))

random=80
flag=[]

for x in range(len(arr2)):
    for c in range(0xff+1):
        if enc(c,random,x) == arr2[x]:
            flag.append(c)
            break

f1=open('flag.jpg', 'wb')
for num in flag:
    f1.write(bytes([num]))

--------------------------------------------------------------------------------









        

