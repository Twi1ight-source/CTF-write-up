import struct

# Read opcodes from file
file = open("bin","rb").read()

def readIns(ip):
	ins = []
	for i in range(3):
		ins.append(file[ip + i])                #đọc 2 byte tiếp theo từ vị trđóđó
	return ins

def onevar(opc, fmt):
	return (fmt % (opc[1]))

def twovar(opc, fmt):
	return (fmt % (opc[1], opc[2]))

def twovarX(opc, fmt):
	t = file[2048 + opc[2]]
	return (fmt % (opc[1], t))

# Opcodes Table
opcodes = {
	1  : ["R%d *= %d", twovar],
	2  : ["R%d -= %d", twovar],
	3  : ["~R%d", onevar],
	4  : ["R%d ^= 0x%.2x", twovarX],
	5  : ["R%d = R%d", twovar],
	6  : ["R%d = 0x%.2x", twovarX],
	7  : ["JMP", None],
	8  : ["PUTC()", None],
	9  : ["exit", None],
	10 : ["R0 = GETC()", None],
	11 : ["R%d << %d", twovar],
	12 : ["R%d &= 0x%.2x", twovarX],
	13 : ["R%d |= 0x%.2x", twovarX],
	14 : ["R%d += R%d", twovar],
}

ip = 0

while(ip < len(file)):
	opc = readIns(ip)

	if opcodes[opc[0]][1] is None:
		print(opcodes[opc[0]][0])
	else:
		desc = opcodes[opc[0]][1](opc, opcodes[opc[0]][0])
		print(desc)

	if(opc[0] == 101 or opc[0] == 9):           #do tại trường hợp 9 là exit 
		break
	
	if (opc[0]==10):
		print('""","""')
    	ip+=3
