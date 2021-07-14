def gcd(a,b):
    if (a==0):
        return [0,1]
    r= gcd(b%a, a)
    return [r[1] - ((b // a) * r[0]), r[0]]

def result(value):
    return ((gcd(value,4294967296)[0] %4294967296) + 4294967296) %4294967296
flag=[]
import string
for a in string.printable:
    for b in string.printable:
        for c in string.printable:
            for d in string.printable:
                value=(((ord(a)<<24)|(ord(b)<<16)) | (ord(c)<<8)) | ord(d)
                if result(value) == 2789358025:
                    flag.append(a,b,c,d)
print(flag)





