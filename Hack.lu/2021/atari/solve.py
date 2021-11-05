L5324=[]
L521A=b'\x43\x11\x37\xF2\x69\xab\x2c\x99\x13\x12\xd1\x7e\x9a\x8f\x0e\x92\x37\xf4\xaa\x4d\x77\x03\x89\xca\xff\x1a'
check=b'\x14\x1e\x0c\xe0\x30\x5c\xce\xf0\x36\xae\xfc\x39\x1a\x91\xce\xb4\xc4\x0e\x18\xf3\xc8\x8e\x0a\x85\xf6\xbd'

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

#def encrypt(inp):
    #for i in range(len(inp)):
        #if i&1==0:
            #res=rol(inp[i] ^ inp[i+1], 1, 8)
        #else:
            #res=rol(inp[i] ^ L521A[i-1], 1, 8)
    #return res

def encrypt1(x,y):
    res=rol(x^y, 1, 8)
    return res

def encrypt2(x,ind):
    res=rol(x^L521A[ind-1], 1, 8)
    return res

inp=[0]*26
import string
for i in range(0,len(inp),2):
    for c in string.printable:
        if encrypt2(ord(c),i+1) == check[i+1]:
            inp[i+1]=ord(c)
            break 
    for c in string.printable:
        if encrypt1(ord(c), inp[i+1]) == check[i]:
            inp[i]=ord(c)
            break

print(bytearray(inp).decode())
        
    



