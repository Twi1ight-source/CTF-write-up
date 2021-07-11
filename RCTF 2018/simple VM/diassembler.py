opcodes=[21, 0, 1, 0, 0, 14, 18, 11, 12, 0, 1, 0, 0, 53, 0, 0, 0, 102, 21, 16, 1, 0, 0, 14, 10, 102, 22, 12, 16, 1, 0, 0, 71, 0, 0, 0, 102, 3, 64, 1, 0, 0, 16, 17, 241, 0, 0, 0, 19, 4, 67, 1, 0, 0, 8, 4, 65, 1, 0, 0, 16, 3, 64, 1, 0, 0, 8, 4, 66, 1, 0, 0, 3, 65, 1, 0, 0, 3, 67, 1, 0, 0, 8, 16, 3, 66, 1, 0, 0, 8, 4, 68, 1, 0, 0, 102, 3, 64, 1, 0, 0, 17, 241, 0, 0, 0, 16, 3, 68, 1, 0, 0, 22, 5, 64, 1, 0, 0, 14, 6, 64, 1, 0, 0, 12, 69, 1, 0, 0, 85, 0, 0, 0, 102, 3, 70, 1, 0, 0, 17, 5, 0, 0, 0, 19, 16, 3, 70, 1, 0, 0, 17, 17, 1, 0, 0, 19, 23, 24, 96, 1, 0, 0, 12, 70, 1, 0, 0, 182, 0, 0, 0, 1, 118, 1, 0, 0, 102]


def parse(i):
	return (hex((opcodes[i+1]) + (opcodes[i+2]<<8) + (opcodes[i+3]<<16) + (opcodes[i+4]<<24)))
def addr(k):
	return hex(k)
def vm_opcode():
	i=0
	while i< len(opcodes):
		k=i+48
		if opcodes[i]==0:
			print(f'{addr(k)}: return {parse(i)}')
			i+=5
		
		elif opcodes[i]==1:
			print(f'{addr(k)}: jmp {parse(i)}')
			i+=5
		
		elif opcodes[i]==2:
			print(f'{addr(k)}: {parse(i)} = {parse(i+5)}')
			i+=9
		
		elif opcodes[i]==3:
			print(f'{addr(k)}: cond = rbp[{parse(i)}]')
			i+=5
		
		elif opcodes[i]==4:
			print(f'{addr(k)}: rbp[{parse(i)}] = rbp(cond)')
			i+=5
		
		elif opcodes[i]==5:
			print(f'{addr(k)}: global = rbp[{parse(i)}]')
			i+=5
		
		elif opcodes[i]==6:
			print(f'{addr(k)}: rbp[{parse(i)}] = global')
			i+=5
		
		elif opcodes[i]==7:
			print(f'{addr(k)}: cond += global')
			i+1
		
		elif opcodes[i]==8:
			print(f'{addr(k)}: cond = ~(global & cond)')
			i+=1
		
		elif opcodes[i]==10:   #0xa
			print(f'{addr(k)}: cond = getchar()')
			i+=1
		
		elif opcodes[i]==11:  #0xb
			print(f'{addr(k)}: putchar(cond)')
			i+=1
		
		elif opcodes[i]==12: #0xc
			print(f'{addr(k)}: rbp[{parse(i)}] ? jmp {parse(i+4)} and --')
			i+=9
		
		elif opcodes[i]==13: #0xd
			print(f'{addr(k)}: cond +=1')
			i+=1
		
		elif opcodes[i]==14:
			print(f'{addr(k)}: global +=1')
			i+=1

		elif opcodes[i]==15:
			print(f'{addr(k)}: cond = global')
			i+=1
		
		elif opcodes[i]==16:
			print(f'{addr(k)}: global = cond')
			i+=1

		elif opcodes[i]==17:
			print(f'{addr(k)}: cond += {parse(i)}')
			i+=5

		elif opcodes[i]==18:
			print(f'{addr(k)}: cond = rbp(global)')
			i+=1

		elif opcodes[i]==19:
			print(f'{addr(k)}: cond = rbp(cond)')
			i+=1

		elif opcodes[i]==20:
			print(f'{addr(k)}: cond = {parse(i)}')
			i+=5
		
		elif opcodes[i]==21:
			print(f'{addr(k)}: global = {parse(i)}')
			i+=5
		
		elif opcodes[i]==22:   #0x16
			print(f'{addr(k)}: [global] = cond')
			i+=1
		
		elif opcodes[i]==23:  #0x17
			print(f'{addr(k)}: cond -= global')
			i+=1
		
		elif opcodes[i]==24: #0x18
			print(f'{addr(k)}: cond ? jmp {parse(i)}')
			i+=5
		
		else:
			print('Nop')
			i+=1

vm_opcode()



