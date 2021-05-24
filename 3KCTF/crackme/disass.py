from os import rename


code=[
R0 = getc
R0 ^= 0x63
R3 += R0
]
for getc in range(40,127):
    R0, R3=0,0
    exec(code)
    if R3==0:
        print(chr(getc))


    