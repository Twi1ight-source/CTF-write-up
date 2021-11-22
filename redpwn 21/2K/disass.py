f=open('prog.bin', 'rb').read()
op=[]
for i in range(len(f)):
    op.append(f[i])

i=0
while i < len(op):
    if op[i]==0x1:
        print('push stack[-1]')
        i+=1

    elif op[i]==0x2:
        print('id-=2')
        i+=1
    
    elif op[i]==0x3:
        print('if stack[-1] !=-1 --> Exit')
        i+=1
    
    elif op[i] ==0x10:
        print('push (pop + pop)')
        i+=1

    elif op[i]==0x11: #17
        print('push (pop -pop)')
        i+=1

    elif op[i]==0x12:
        print('push (pop * pop)')
        i+=1

    elif op[i]==0x13:
        print('push (pop / pop)')
        i+=1

    elif op[i]==0x14:
        print('push (pop % pop)')
        i+=1

    elif op[i]==0x15:
        print('a=pop, b=pop, c= pop ')
        print('  push ( (b*c) mod a )')
        i+=1

    elif op[i]==0x16:
        print('a=pop, b=pop')
        print('if a==b:')
        print('  stack[-2]= 1')
        print('else:')
        print('  stack[-2]= 0')
        i+=1
    
    elif op[i]==0x17:
        print('if stack[-1] ==0:')
        print('  stack[-1]= -1')
        print('else:')
        print('  stack[-1]= 1')
        i+=1

    elif op[i]==0x20: #32
        print('getc')
        i+=1

    elif op[i]==0x21: #33
        print(f'print')
        i+=1

    elif op[i]==0x22: #34
        print(f'push {op[i+1]}')
        i+=3

    elif op[i]==0x30: #48
        print('not_useful')
        i+=1

    elif op[i]==0x31:
        print('if stack[-2]!= 0 -->ok')
        i+=1

    elif op[i]==0x32:
        print('if stack[-2]== 0 -->ok')
        i+=1

    elif op[i]==0x34:
        print('if stack[-2]<= 0 -->ok')
        i+=1
    
    elif op[i]==0x36:
        print('if stack[-2]< 0 -->ok')
        i+=1

    elif op[i]==0x40: #64
        print('mem[cx] = pop')
        i+=1
    
    elif op[i]==0x41:
        print('stack[-1]= mem[cx]')
        i+=1
    
    elif op[i]==0x50: #80
        print('cx+=1')
        i+=1
    
    elif op[i]==0x51: 
        print('cx-=1')
        i+=1
    
    elif op[i]==0x52: 
        print('cx+= stack[-1]')
        i+=1

    elif op[i]==0x53:
        print('cx-= stack[-1]')
        i+=1

    else:
        print('Error')
        break

