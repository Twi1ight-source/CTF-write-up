```python
from capstone import *
from capstone.x86 import *
import pwn
import pefile

md=Cs(CS_ARCH_X86, CS_MODE_64)
pwn.context.arch='amd64'

md.detail=True

pe=pefile.PE("tttree2.exe")
c=bytearray(open("tttree2.exe","rb").read())

def patch(chunk: bytearray)-> bytearray:
    pattern = b'\x50\x50\x9c'   #push rax, push rax, pushfq
    for off in range(len(chunk)):
        if chunk[off:off+len(pattern)]==pattern:
            inss=md.disasm(chunk[off:off+0x40],0)
    
            adr_v=[]
            for i in inss:
                print(i)
                if i.mnemonic=='add':
                    assert i.address in [0x9,0x1f]
                    assert i.mnemonic=='add'
                    adr_v.append(i.operands[1].value.imm)      
                
                if i.address==0x16:
                    if i.mnemonic=='ret':               
                        assert len(adr_v)==1
                        target=adr_v[0]+8

                        n=i.address+i.size              
                        chunk[off:off+n]=b'\x90'*n      #patch from current off to ret with NOPs
                                                
                        jins=pwn.asm(f"jmp $+{target}")
                        chunk[off:off+len(jins)]=jins
                        break
                    else:
                        assert chunk[off+0x16:off+0x16+len(pattern)]==pattern  #case 2
                
                if i.address==0x16*2:
                    assert i.mnemonic=='ret'
                    assert len(adr_v)==2
                    call_target=adr_v[0]+8
                    jmp_target=adr_v[1]+0x1e

                    shc = pwn.asm(f'''
                            call $+{jmp_target}
                            ''')
                    shj = pwn.asm(f'''
                            jmp $+{call_target}
                            ''')


                    n=i.address+i.size
                    chunk[off:off+n]=b'\x90'*n

                    jins=shc+shj
                    chunk[off:off+len(jins)]=jins
                    break
    return chunk


                
for s in pe.sections:
    if not (s.IMAGE_SCN_MEM_EXECUTE):
        continue
    l = s.PointerToRawData
    r = l + s.SizeOfRawData
    c[l:r]=patch(c[l:r])

open('pat.exe','wb').write(c)

```
