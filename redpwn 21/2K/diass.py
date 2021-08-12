opc=open('prog.bin', 'rb').read()

i=0
while(i<len(opc)):
    if opc[i]==1:
        print('{i}: ({opc[i]}) push stack[-1]')
        i+=1
    elif opc[i]==2:
        print(f'{i}: ({opc[i]}) pop()')
        i+=1
    elif opc[i]==3:
        print(f'{i}: ({opc[i]}) exit if stak[-1] =0')
        i+=1
    elif opc[i]==0x10:
        print(f'{i}: ({opc[i]}) pop() + pop()')
        i+=1
    elif opc[i]==0x11:
        print(f'{i}: ({opc[i]}) pop() - pop()')
        i+=1
    elif opc[i]==0x12:
        print(f'{i}: ({opc[i]}) pop() * pop()')
        i+=1
    elif opc[i]==0x13:
        print(f'{i}: ({opc[i]}) pop() // pop()')
        i+=1
    elif opc[i]==0x14:
        print(f'{i}: ({opc[i]}) pop() % pop()')
        i+=1
    elif opc[i]==0x15:
        print(f'{i}: ({opc[i]}) a=pop(), b=pop(), c=pop()')
        print(f'    (c*b) %a')
        i+=1
    elif opc[i]==0x16:
        print(f'{i}: ({opc[i]}) a=stack[-1], b=stack[-2]')
        print(f'  if a==b:')
        print(f'    b=1')
        print(f'  else:')
        print(f'    b=0')
        print(f'  pop()')
        i+=1
    elif opc[i]==0x17:
        print(f'{i}: ({opc[i]}) check if stack[-1] ==0')
        i+=1
    elif opc[i]==0x20:
        print(f'{i}: ({opc[i]}) getc()')
        i+=1
    elif opc[i]==0x21:
        print(f'{i}: ({opc[i]}) print()')
        i+=1
    elif opc[i]==0x22:
        print(f'{i}: ({opc[i]}) push {opc[i+1]}, {opc[i+2]}')
        i+=3
    elif opc[i]==0x30:
        print(f'{i}: ({opc[i]}) not useful')
        i+=1
    elif opc[i]==0x31:
        print(f'{i}: ({opc[i]}) if stack[-2]!=0: jmp stack[-1]')
        i+=1
    elif opc[i]==0x32:
        print(f'{i}: ({opc[i]}) if stack[-2]==0: jmp stack[-1]')
        i+=1
    elif opc[i]==0x33:
        print(f'{i}: ({opc[i]}) if stack[-2]<0: jmp stack[-1]')
        i+=1
    elif opc[i]==0x34:
        print(f'{i}: ({opc[i]}) if stack[-2]<=0: jmp stack[-1]')
        i+=1
    elif opc[i]==0x35:
        print(f'{i}: ({opc[i]}) if stack[-2]>0: jmp stack[-1]')
        i+=1
    elif opc[i]==0x36:
        print(f'{i}: ({opc[i]}) if stack[-2]>=0: jmp stack[-1]')
        i+=1
    elif opc[i]==0x40:
        print(f'{i}: ({opc[i]}) mem[cx]= pop()')
        i+=1
    elif opc[i]==0x41:
        print(f'{i}: ({opc[i]}) push mem[cx]')
        i+=1
    elif opc[i]==0x50:
        print(f'{i}: ({opc[i]}) cx++')
        i+=1
    elif opc[i]==0x51:
        print(f'{i}: ({opc[i]}) cx--')
        i+=1
    elif opc[i]==0x52:
        print(f'{i}: ({opc[i]}) cx+= pop()')
        i+=1
    elif opc[i]==0x53:
        print(f'{i}: ({opc[i]}) cx-=pop()')
        i+=1
    else:
        print("Nope")
        i+=1
    
