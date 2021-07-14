from itertools import permutations
def gcd(a,b):
    if (a==0):
        return [0,1]
    r= gcd(b%a, a)
    return [r[1] - ((b // a) * r[0]), r[0]]

def result(value):
    return ((gcd(value,4294967296)[0] %4294967296) + 4294967296) %4294967296
flag=[]


pos=permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!_{}?0123456789',4)
for c in pos:
    i0,i1,i2,i3=c
    value=(((ord(i3)<<24) | (ord(i2)<<16)) | (ord(i1)<<8)) | ord(i0)
    if result(value) == 2789358025:
        flag.append([i0,i1,i2,i3])
print(flag)





