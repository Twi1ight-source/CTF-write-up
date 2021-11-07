from z3 import *

k=[BitVec(f'{i}',16) for i in range(16)]
s=Solver()
for c in k:
    s.add(c>0x20,c<0x7f)

s.add(k[0]==ord('f'))
s.add(k[1]==ord('l'))
s.add(k[2]==ord('a'))
s.add(k[3]==ord('g'))
s.add(k[4]==ord('{'))
s.add(k[10]==ord('e'))
s.add(k[11]== ord('7'))
s.add(k[15]==ord('}'))

s.add(k[6]+k[7]+k[10]==260)
s.add(k[5]==sum(k) -1322)
s.add(Or(k[9]==33+1, k[9]==44+1, k[9]==55+1, k[9]==66+1, k[9]==77+1, k[9]==88+1, k[9]==99+1))
s.add(Or(k[7]==ord('3'), k[7]==ord('4'), k[7]==ord('5'), k[7]==ord('6'), k[7]==ord('7'), k[7]==ord('8'), k[7]==ord('9')))
s.add(k[8]%17 ==16)
s.add(k[9] ==k[8]*2)
s.add(k[12]==(k[14] >>1) -2)
s.add(k[13]== ((k[10]*k[8]) %32) *2 -1)
s.add(k[14]==(k[12] ^k[9] ^ k[15]) *3 -23)
s.add(k[5] == ord('5'))

print(s.check())
if s.check() == sat:
    m=s.model()
    for j in k:
        print(chr(m[j].as_long()), end="")





