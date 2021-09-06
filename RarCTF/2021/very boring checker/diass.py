from ctypes import *

def check(a1):
    ip,v11=0,0
    mem_ptr, stack_ptr, inp_ptr =0,0,0
    stack = []
    for i in range(256):
        stack.append(c_uint8(0))

    mem = []
    for i in range(256):
        mem.append(c_int(0))
    

    while ip < len(code):
        a=(code[ip]>>7)>>5
        ins=(a+ code[ip])&7 -a 

        if not v11:
            if ins==0:
                print(f'stack_ptr+=1 ({stack_ptr}+=1)')
                stack_ptr+=1
                

            elif ins==1:
                print(f'{ip, ins}: if (stack[{stack_ptr}]({stack[stack_ptr].value})): ip=mem[mem_ptr-1](ip={mem[mem_ptr-1].value})')
                print(f'           else: mem[mem_ptr-1]=0({mem[mem_ptr-1].value}), mem_ptr--({mem_ptr}--)')
                if (stack[stack_ptr].value !=0):
                    ip=mem[mem_ptr-1].value
                else:
                    mem_ptr-=1
                    mem[mem_ptr].value=0
                
            
            elif ins==2:
                print(f'{ip, ins}: stack_ptr-=1 ({stack_ptr}-=1)')
                stack_ptr-=1
                
            
            elif ins==3:
                print(f'{ip, ins}: if stack[{stack_ptr}] ({stack[stack_ptr].value}): mem[mem_ptr]=ip (={ip}), mem_ptr+=1 ({mem_ptr}+=1)')
                print(f'              else: v11+=1 ({v11}+=1)')
                if (stack[stack_ptr].value!=0):
                    mem[mem_ptr].value=ip
                    mem_ptr+=1
                    
                else:
                    v11+=1
                

            elif ins==4:
                print(f'{ip, ins}: if not inp_ptr({inp_ptr}): input()')
                
                if not inp_ptr:
                    inp= a1+ '\n'.ljust(64, '\x00')
                stack[stack_ptr].value=ord(inp[inp_ptr])
                print(f'stack[{stack_ptr}]= inp[inp_ptr](={ord(inp[inp_ptr])})')
                inp_ptr+=1
                    
            
            elif ins==5:
                print(f'{ip, ins}: putchar({chr(stack[stack_ptr].value)})')
                
            elif ins==6:
                print(f'{ip, ins}: stack[{stack_ptr}]-=1 ({stack[stack_ptr].value}-=1)')
                stack[stack_ptr].value-=1
                
            elif ins==7:
                print(f'{ip, ins}: stack[{stack_ptr}]+=1 ({stack[stack_ptr].value}+=1)')
                stack[stack_ptr].value+=1
               
            else:
                break
        else:
            if ins==3:
                v11+=1
                
            elif ins==1:
                v11-=1

        ip+=1  

code=open('prog.bin', 'rb').read()
check('rarctf'+'a'*49)
