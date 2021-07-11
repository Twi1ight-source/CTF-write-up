def operation(c,i):
    i+=32
    X= ~(i &c) &0xff
    Y= ~(X & i) &0xff
    Z= ~ (X & c) &0xff
    T= ~(Z & Y) &0xff
    return T

enc=[16, 24, 67, 20, 21, 71, 64, 23, 16, 29, 75, 18, 31, 73, 72, 24, 83, 84, 1, 87, 81, 83, 5, 86, 90, 8, 88, 95, 10, 12, 88, 9]
flag=""
import string
for i in range(32):
    for c in string.printable:
        if operation(ord(c),i) == enc[i]:
            flag+=c
print(flag)

