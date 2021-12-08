check=[
(1, 0, 0, 1, 0, -1, 1, -1, -1, 0, 0, -1, 0, 0, -1, 1),
(1, 1, 1, 0, -1, 0, -1, -1, 1, 1, -1, 1, 0, 0, 0, -1),
(0, 0, 1, 0, -1, 1, -1, -1, 0, 0, 1, 1, -1, -1, 0, -1),
(0, 1, 0, 1, -1, -1, 1, 0, -1, 0, 1, 1, 1, -1, -1, 0),
(0, 0, 0, 0, -1, 1, 0, -1, -1, -1, 1, 1, -1, -1, 0, 0),
(0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, -1, 1, -1, 0),
(0, 1, 0, 1, -1, -1, 1, 0, -1, 0, 1, 1, 1, -1, -1, 0),
(-1, 0, -1, 1, 1, 1, -1, 0, 1, -1, -1, 0, -1, 0, 1, 1),
(0, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 0, 1, -1, 0),
(0, 0, 0, 0, -1, 1, 0, -1, -1, -1, 1, 1, -1, -1, 0, 0),
(0, 0, 1, 1, -1, 1, -1, 0, 1, 1, -1, 1, 1, 1, -1, -1),
(0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, -1, 1, -1, 0),
(-1, 1, 0, -1, 1, 1, 1, 0, 1, -1, 0, 0, -1, 1, 0, -1),
(0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, -1, 1, -1, 0),
(0, 0, 0, 0, -1, 1, 0, -1, -1, -1, 1, 1, -1, -1, 0, 0),
(0, 0, -1, 1, -1, 0, 0, 0, -1, -1, -1, 1, -1, 1, 1, -1),
(0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, -1, 1, -1, 0),
(0, 0, 1, 0, -1, 1, -1, -1, 0, 0, 1, 1, -1, -1, 0, -1),
(0, 0, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 0, 1, 0, 0),
(0, 0, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 0, 1, 0, 0),
(0, -1, 0, 0, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, 0, -1),
(0, -1, 0, -1, 1, 1, 0, 1, -1, 1, 1, 0, 0, 1, -1, -1),
(0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, -1, 1, -1, 0),
(0, 0, 1, -1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, -1),
(0, 0, 0, 0, -1, 1, 0, -1, -1, -1, 1, 1, -1, -1, 0, 0),
(0, 0, -1, 1, -1, 0, 0, 0, -1, -1, -1, 1, -1, 1, 1, -1),
(1, 1, 1, 0, -1, 0, -1, -1, 1, 1, -1, 1, 0, 0, 0, -1),
(0, 0, 1, 0, -1, 1, -1, -1, 0, 0, 1, 1, -1, -1, 0, -1),
(0, 1, 0, 1, -1, -1, 1, 0, -1, 0, 1, 1, 1, -1, -1, 0),
(0, 0, 0, 0, -1, 1, 0, -1, -1, -1, 1, 1, -1, -1, 0, 0),
(1, 1, 1, 1, -1, 1, 1, 0, -1, 0, 0, -1, 1, 0, -1, 1),
(0, -1, 1, -1, 1, 0, 1, -1, -1, 0, -1, -1, 0, 0, -1, -1),
(1, 1, 1, 0, -1, 0, -1, -1, 1, 1, -1, 1, 0, 0, 0, -1),
(0, -1, -1, -1, 1, -1, 1, 1, -1, -1, 0, 0, 0, -1, -1, 0),
(0, 0, -1, -1, -1, -1, -1, 1, 1, 0, -1, -1, 0, -1, -1, 1)
]

import random
import string

flag=""
id=0
while id <35:
    ch=False
    check1=check[id]
    for c in string.printable:
        random.seed(c)
        count=-1
    
        for i in range(16):
            if random.randint(-1,1) == check1[i]:
                count+=1
            else:
                break
        
            if count==15:
                flag+=c
                ch=True

        if ch==True:
            break
    id +=1

print(flag[::-1])
