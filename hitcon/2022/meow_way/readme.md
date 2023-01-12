```python
#  0x0 [4831c0]: xor rax, rax>
#  0x3 [65488b4060]: mov rax, qword ptr gs:[rax + 0x60]> #PEB
#  0x8 [480fb64002]: movzx rax, byte ptr [rax + 2]>      #PEB->BeingDebugged
#  0xd [678b4c241c]: mov ecx, dword ptr [esp + 0x1c]>   #ts4-> empty buffer
#  0x12 [678901]: mov dword ptr [ecx], eax>
#  0x15 [85c0]: test eax, eax>            #anti-debug
#  0x17 [7518]: jne 0x31>
#  0x19 [678b7c2404]: mov edi, dword ptr [esp + 4]>     #ts1-> inp
#  0x1e [678b74240c]: mov esi, dword ptr [esp + 0xc]>   #ts2-> inp
#  0x23 [678b4c2414]: mov ecx, dword ptr [esp + 0x14]>  #ts3-> const
#  0x28 [67020e]: add cl, byte ptr [esi]>     #ts3+=ts2
#  0x2b [80f1ba]: xor cl, 0xba>
#  0x2e [67880f]: mov byte ptr [edi], cl>
#  0x31 [e800000000]: call 0x36>
#  0x36 [c744240423000000]: mov dword ptr [rsp + 4], 0x23>   #return x86 code
#  0x3e [8304240d]: add dword ptr [rsp], 0xd>
#  0x42 [cb]: retf >
#  0x43 [c3]: ret >

#-----------------------------------------------------------------------------

import idautils
import idc

def get_code(addr):
    xref=list(idautils.DataRefsTo(addr))[0]
    #print(hex(xref))
    #ins=idc.generate_disasm_line(xref,0)
    func_addr=idc.get_operand_value(xref,1)
    # print(func_addr)
    code=idaapi.get_bytes(func_addr+0xc,76)
    code=code[:code.find(b"\xc3")+1]
    return code

from capstone import *
from capstone.x86 import *

md= Cs(CS_ARCH_X86, CS_MODE_64)

addr_list={2577484: 196, 2577320: 22, 2577332: 142, 2577392: 119, 2577480: 5, 2577404: 185, 2577408: 13, 2577424: 107, 2577400: 36, 2577456: 85, 2577360: 18, 2577460: 53, 2577500: 118, 2577492: 231, 2577344: 251, 2577380: 160, 2577348: 218, 2577472: 52, 2577340: 132, 2577324: 180, 2577416: 200, 2577368: 155, 2577336: 239, 2577352: 180, 2577376: 185, 2577432: 10, 2577388: 87, 2577428: 92, 2577488: 254, 2577384: 197, 2577364: 106, 2577436: 115, 2577452: 73, 2577476: 189, 2577496: 17, 2577440: 214, 2577328: 143, 2577372: 107, 2577508: 10, 2577356: 151, 2577444: 171, 2577468: 78, 2577412: 237, 2577448: 254, 2577504: 151, 2577420: 249, 2577396: 152, 2577464: 101}
flag=""
check=b"\x96P\xcf,\xeb\x9b\xaa\xfbS\xabs\xddl\x9e\xdb\xbc\xee\xab#\xd6\x16\xfd\xf1\xf0\xb9u\xc3(\xa2t}\xe3'\xd5\x95\\\xf5vu\xc9\x8c\xfbB\x0e\xbdQ\xa2\x98"
count=0

for ad in addr_list:
    status=0
    complete=0
    code=get_code(ad)
    #print(code)
    for ins in md.disasm(code,0):
        ins_str= ins.op_str
        
        if ins.mnemonic=='add' and 'cl' in ins_str:
            status=1
        elif ins.mnemonic=='sub' and 'cl' in ins_str:
            status=2
        
        if ins.mnemonic=="xor" and 'cl' in ins_str:
            xor_val= int(ins_str.replace("cl, ",""),16)
            complete=1

        if complete==1:
            if status==1:
                flag+=chr(((check[count]^xor_val) -addr_list[ad])&0xff)
            if status==2:
                flag+=chr((addr_list[ad]- (check[count]^xor_val) )&0xff)
            break

    count+=1

print(flag)
```
