```python
from keystone import *

def ReadData():
    f = open("trace.txt", "r")
    data = f.read().split("\n")
    return data

def ReconstructShellCode():
    data = ReadData()
    assembler = Ks(KS_ARCH_X86, KS_MODE_64)
    assemblyAddr = []
    
    #Init code mem (base 0x401000)
    codeMem = []
    for i in range(0, 0x1000):
        codeMem.append(0x90)
    
    for line in data:
        if line == "":
            continue
            
        tmp = line.split(" : ")
        addr = int(tmp[0], 16)
        code = tmp[1]
        if addr not in assemblyAddr:
            try:
                #Some quick fix
                print(code)
                if ", ptr" in code:
                    code = code.replace(", ptr", ", ")
                ops, cnt = assembler.asm(code, addr)
                print(hex(addr))
            except KsError as e:
                print("ERROR: %s" %e)
                print(code)
                break
            
            print(ops)
            for i in range(0, len(ops)):
                codeMem[addr - 0x401000 + i] = ops[i]
            
            assemblyAddr.append(addr)
    
    #print(codeMem)
    shellcodeFile = open("shellcode1.bin", "wb")
    shellcodeFile.write(bytearray(codeMem))
    shellcodeFile.close()
    print("Reconstruct shellcode OK")
    
if __name__ == "__main__":
    ReconstructShellCode()
```
