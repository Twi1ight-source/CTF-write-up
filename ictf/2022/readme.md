##Parse ast tree:

```python
from ast import *
txt=open("").read().strip
txt='tree='+txt[1:-1]
exec(txt)
fix=fix_missing_locations(txt)
src=unparse(fix)
open('src.py','w').write(src)
```

##Brute:

```python
ck=[123, 250, 94, 95, 121, 195, 249, 70, 71, 59, 137, 59, 5, 67, 65, 226, 17, 160, 205, 100, 251, 169, 50, 118, 184, 177, 1, 175, 133]

import os

idx=5
ori='ictf{'
while True:
    if idx==29:
        break
    for c in range(0x30,0x7f):
        
        if c==96:
            continue
        mod=ori+chr(c)*(29-idx)
        print(mod)
        os.system(f"echo \"{mod}\" | python3.9 src1.py > log.txt")

        f=open('log.txt').read().replace("flag? [","").replace(']','').replace('\n','')
        f=f.split(', ')
        
        if int(f[idx])==ck[idx]:
            print(f'Found: {chr(c)}')
            print(idx)
            idx+=1
            ori+=chr(c)
            break

print(ori)
```

