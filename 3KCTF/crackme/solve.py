
with open('p.bin', 'rb') as f:
    opcode=f.read()

data = opcode[2048:]
rbp = [0]*4



def print_info(op, i, rax, rbx):
    print(f"\n\n[*] opcode: {op}, idx: {i}", end=', ')
    if op != 0:
        print(f'rax: {rax}, rbx: {rbx}')
    print("----------------------------------\n")
    print("--> ", end='')

def vm_opcode():
    i = 0
    while i <= 1215:
        
        rax = opcode[i+1]
        rbx = opcode[i+2]
       
        print_info(opcode[i], i, rax, rbx)

        if opcode[i] == 1:
            print(f'[rbp+{rax}] *= rbx  ; [rbp+{rax}] *= {rbx}')

        elif opcode[i] == 2:
            print(f'[rbp+{rax}] -= rbx  ; [rbp+{rax}] -= {rbx}')
            

        elif opcode[i] == 3:      
            print(f'~ [rbp+{rax}]  ; [rbp+{rax}] ^ 0xff')
            

        elif opcode[i] == 4:
            print(f'[rbp+{rax}]  ^= [data+{rbx}]  ;  [rbp+{rax}] ^= {data[rbx]}')
            

        elif opcode[i] == 5:
            print(f'[rbp+{rax}] = [rbp+{rbx}]')
            

        elif opcode[i] == 6:
            print(f'[rbp+{rax}] = [data+{rbx}]  ;  [rbp+{rax}] = {data[rbx]}')
            

        elif opcode[i] == 7:
            print(f'cmp [rbp+{rbx}], 0')
            print(f'--> jnz [opcode_list+{i+rax}]  ;  jnz {i + rax}')

        elif opcode[i] == 8:
            print(f'putc([rbp+{rax}])')

        elif opcode[i] == 9:
            print(f'exit()')

        elif opcode[i] == 10:
            
            print(f'getc([rbp+{rax}])')
            

        elif opcode[i] == 11:
            print(f'[rbp+{rax}] = [rbp+{rax}] << {rbx}')
            

        elif opcode[i] == 12:
            print(f'[rbp+{rax}] &= [data+{rbx}]  ;   [rbp+{rax}] &= {data[rbx]}')
            

        elif opcode[i] == 13:
            print(f'[rbp+{rax}] |= [data+{rbx}]  ;   [rbp+{rax}] |= {data[rbx]}')
            

        elif opcode[i] == 14:
            print(f'[rbp+{rax}] += [rbp+{rbx}]')
            
        
        i+=3

vm_opcode()