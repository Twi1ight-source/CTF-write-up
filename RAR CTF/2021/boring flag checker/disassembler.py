f=open('prog.bin', 'rb').read()
opcode=[]
for i in range(len(f)):
    opcode.append(f[i])


id=0
v4=0
v15=0
v1c=0
v540=[0]*280
v130=[0]*280
v10=0
buf=b'rarctf{asd123'
while id < len(opcode):
    
    while (True):
        if v1c==0:
            break
        opc=(opcode[id] + ((opcode[id]>>7)>>5))&7 - ((opcode[id]>>7)>>5)
        if opc==1:
            v1c-=1
        if opc==3:
            v1c+=1
        id+=1

    opc=(opcode[id] + ((opcode[id]>>7)>>5))&7 - ((opcode[id]>>7)>>5)
    
    if opc==0:
        #print('case 0')
        v4=(v4+1)&0xff
        id+=1

    elif opc==1:
        #print('case 1')
        if v130[v4]!=0:
            id=v540[(v15-1)&0xff]
        else:
            v540[(v15-1)&0xff]=0
            v15=(v15-1)&0xff
        id+=1

    elif opc==2:
        #print('case 2')
        v4=(v4-1)&0xff
        id+=1

    elif opc==3:
        #print('case 3')
        if v130[v4] !=0:
            v540[v15]=id
            v15=(v15+1)&0xff
        else:
            v1c=(v1c+1)&0xff
        id+=1

    elif opc==4:
        #print('case 4')
        if v10<=len(buf)-1:
            print(f'get({chr(buf[v10])})')
            v130[v4]=buf[v10]
            v10+=1
        id+=1

    elif opc==5:
        #print('case 5')
        print(chr(v130[v4]))
        id+=1

    elif opc==6:
        #print('case 6')
        v130[v4]=(v130[v4]-1)&0xff
        id+=1
    
    elif opc==7:
        #print('case 7')
        v130[v4]=(v130[v4]+1)&0xff
        id+=1
    
    else:
        print('Error !!!!')
        break
    
    

