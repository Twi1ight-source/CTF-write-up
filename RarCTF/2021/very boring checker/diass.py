
def check(a1):
    ip,v11=0,0
    mem_ptr, stack_ptr, inp_ptr =0,0,0
    stack = [0]*256
    mem = [0]*256
    
    while ip < len(code):
        a=(code[ip]>>7)>>5
        ins=(a+ code[ip])&7 -a 

        if not v11:
            if ins==0:
                print(f'stack_ptr+=1 ({stack_ptr}+=1)')
                stack_ptr+=1
                

            elif ins==1:
                print(f'{ip, ins}: if (stack[{stack_ptr}]({stack[stack_ptr]})): ip=mem[mem_ptr-1](ip={mem[mem_ptr-1]})')
                print(f'           else: mem[mem_ptr-1]=0({mem[mem_ptr-1]}), mem_ptr--({mem_ptr}--)')
                if (stack[stack_ptr] !=0):
                    ip=mem[mem_ptr-1]
                else:
                    mem_ptr-=1
                    mem[mem_ptr]=0
                
            
            elif ins==2:
                print(f'{ip, ins}: stack_ptr-=1 ({stack_ptr}-=1)')
                stack_ptr-=1
                
            
            elif ins==3:
                print(f'{ip, ins}: if stack[{stack_ptr}] ({stack[stack_ptr]}): mem[mem_ptr]=ip (={ip}), mem_ptr+=1 ({mem_ptr}+=1)')
                print(f'              else: v11+=1 ({v11}+=1)')
                if (stack[stack_ptr]!=0):
                    mem[mem_ptr]=ip
                    mem_ptr+=1
                    
                else:
                    v11+=1
                

            elif ins==4:
                print(f'{ip, ins}: if not inp_ptr({inp_ptr}): input()')
                
                if not inp_ptr:
                    inp= a1+ '\n'.ljust(64, '\x00')
                stack[stack_ptr]=ord(inp[inp_ptr])
                print(f'stack[{stack_ptr}]= inp[inp_ptr](={ord(inp[inp_ptr])})')
                inp_ptr+=1
                    
            
            elif ins==5:
                print(f'{ip, ins}: putchar({chr(stack[stack_ptr])})')
                
            elif ins==6:
                if stack[stack_ptr]<0:
                    stack[stack_ptr]=255        
                print(f'{ip, ins}: stack[{stack_ptr}]-=1 ({stack[stack_ptr]}-=1)')
                stack[stack_ptr]-=1
                
                   
            elif ins==7:
                if stack[stack_ptr] ==255:
                    stack[stack_ptr]=-1
                print(f'{ip, ins}: stack[{stack_ptr}]+=1 ({stack[stack_ptr]}+=1)')
                stack[stack_ptr]+=1
               
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
