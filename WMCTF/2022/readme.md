## Archgame 

```python
import gdb
import os


pos=[0x4ADCA886, 0x95F2E403, 0xA19A4E46, 0x6553AD74, 0xCC3E290C, 0x3B2884A6]

base=0x00555555554000

found=[]
for i in range(len(pos)):
    gdb.execute("file ./ArchGam")

    gdb.execute(f"break *{base+0x32C073}")
    gdb.execute(f"break *0x5555558800B8")
    gdb.execute(f"r <<< $(echo 'aa')")
    gdb.execute(f"set $rax=0x76EAB3E1")     #chall14
    gdb.execute('c')
    gdb.execute('d')

    gdb.execute(f"break *{base+0x32C073}")
    gdb.execute(f"break *0x5555558800B8")
    gdb.execute('c')
    gdb.execute(f"set $rax=0xB8D86C63")     #chall12
    gdb.execute('c')
    gdb.execute('d')  

    gdb.execute(f"break *{base+0x32C073}")
    gdb.execute(f"break *0x5555558800B8")
    gdb.execute('c')
    gdb.execute(f"set $rax=0x5CBECC04")     #chall33
    gdb.execute('c')
    gdb.execute('d')  

    gdb.execute(f"break *{base+0x32C073}")
    gdb.execute(f"break *0x5555558800B8")
    gdb.execute('c')
    gdb.execute(f"set $rax=0x249d8564")     #chall36
    gdb.execute('c')
    gdb.execute('d')  
   
    
    gdb.execute(f"break *{base+0x32BC0A}")  #arch,mode
    gdb.execute(f"break *{base+0x32C073}")  #return value
    gdb.execute(f"break *{base+0x32BB46}")   #chall
    gdb.execute(f"break *{base+0x32BBDA}")  #global_key
    gdb.execute("c")



    reg=str(gdb.parse_and_eval("$rdi"))
    chall=gdb.inferiors()[0].read_memory(int(reg,16),18).tobytes()
    gdb.execute("continue")

    mode=gdb.parse_and_eval("$rcx")
    arch=gdb.parse_and_eval("$rax")
    gdb.execute("continue")

    gdb.execute(f"set $rax={str(pos[i])}")
    

    try:
        gdb.execute("continue")
        global_key=gdb.parse_and_eval("$rax")
    except:
        continue
    uwu=([hex(pos[i]), hex(global_key), str(chall.decode()), str(arch), str(mode)])
    gdb.execute("d")
    gdb.execute(f"break *{base+0x32BB46}")  #chall
    gdb.execute(f"break *{base+0x32BC0A}")  #arch,mode

    gdb.execute("c") 
    reg=str(gdb.parse_and_eval("$rdi"))
    chall=gdb.inferiors()[0].read_memory(int(reg,16),18).tobytes()

    gdb.execute('c')
    mode=gdb.parse_and_eval("$rcx")
    arch=gdb.parse_and_eval("$rax")

    found.append([str(chall.decode()), str(arch), str(mode)]+uwu)

print(found)
found1=""
for i in found:
    found1+=str(i)+'\n'
open('found.txt', 'w').write(found1)
gdb.execute('q')
```
