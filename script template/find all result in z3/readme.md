```python
from z3 import *
from pwn import *
import sys

FLAG = "HTB{g3tt1ng_%s_part3_part4}"

s = Solver()
flag = []
for x in range(6):
    c = BitVec('f%d'%x, 8)
    flag.append(c)
    s.add(
            Or(
                And(c >= 48, c < 65),
                And(c > 90, c <= 122)
            )
            )

s.add(flag[0] + flag[1] + flag[2] + flag[3] + flag[4] + flag[5] == 0x223)
s.add(((((flag[0] * 3 + flag[1]) * 3 + flag[2]) * 3 + flag[3]) * 3 + flag[4]) * 3 + flag[5] == 0x8dd3)

s.add(flag[0] + flag[5] == 0xdf)
s.add(flag[1] + flag[4] == 0xdd)
s.add(flag[2] + flag[3] == 0x67)



context.log_level = 'error'

def check(password):
    io = process("./ffi")
    io.sendline(bytes(FLAG%password, 'ascii'))
    if b'Rust says no!' not in io.recv(1024):
        print(FLAG%password)
        sys.exit(0)

    io.close()



while s.check() == sat:
    m = s.model()
    condition = []

    out = ""
    for x in range(len(flag)):
        c = m[flag[x]].as_long()
        out += chr(c)

        condition.append(flag[x] != int(m[flag[x]].as_long()))
    s.add(Or(condition))

    check(out)
 ```
