flag=[[0 for i in range(8)]  for i in range(400) ]
f=open('res.txt', 'r').read()
f1=f.split('\n')
for line in range(0,len(f1),5):
    if 'mov     cx' in f1[line]:
        a=f1[line].replace('mov     cx, [edi+','')
        if 'h]' in a:
            a=a.replace('h]', '')
        else:
            a=a.replace(']', '')
        tmp1=int(f'0x{a}',16)
        
    
    if 'shr     cx' in f1[line+1]:
        a=f1[line+1].replace('shr     cx, ','')
        tmp2=7-int(a)
    
    if 'cmp     cx' in f1[line+3]:
        a=f1[line+3].replace('cmp     cx, ','')
        tmp3=int(a)

    flag[tmp1][tmp2] =tmp3

for i in flag:
    khai=''
    for j in i:
        khai+=str(j)
    print(chr(int(khai,2)),end="")


    



    
        