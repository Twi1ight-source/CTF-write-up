
enc='\x18j|a\x118i7[H~Jh^Ko\x1f]\x5cw4kP\x15pO?\x5cEo\x14\x06\x05}>=\x04\x16.\x12L'
enc_flag=[]
for i in enc:
    enc_flag.append(ord(i))


#hieu qua trinh encrpyt sau khi debug:
#for i in range(len(47)):
#  if i=1,2 -->x=(inp[i]^20) ^ inp[i-1]), else -->x=inp[i-3] ^ (inp[i]^20)
#  y=i%10
#  z=x^y
#  if i%2==0 -->t=z ^ 9, else -->t=z^8
#  if i%3==0 -->m=t ^ 7, elif i%3==1 -->m=z^6, else--> m=z^5

from z3 import *
flag_buffer=[0]*41
def enc(inp):
    for i in range(41):
        flag_buffer[i]=inp[i]^20
        if i>0:
            flag_buffer[i]^=flag_buffer[i-1]
        if i>=3:
            flag_buffer[i]^=flag_buffer[i-3]

        flag_buffer[i]^=i%10

        if i%2==0:
            flag_buffer[i]^=9
        else:
            flag_buffer[i]^=8
            
        if i%3==0:
            flag_buffer[i]^=7
        else:
            if i%3==1:
                flag_buffer[i]^=6
            else:
                flag_buffer[i]^=5

    #swap
    for i in range(0,40,2):
        flag_buffer[i], flag_buffer[i+1]=flag_buffer[i+1], flag_buffer[i]
        
    return flag_buffer


flag=[BitVec(f'flag{i}', 8) for i in range(41)]
s=Solver()

for i in range(41):
    s.add(enc(flag)[i]==enc_flag[i])

if s.check()==sat:
    model=s.model()
    for i in flag:
        c=model[i].as_long()
        print(chr(c),end="")

