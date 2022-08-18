## Hackermans

Script brute SHA-256:

```python
target_hash=b"\x9c\x00\xf1\xaccb\x16\xe24/d\xae;\x82\xe3\xc0'I\xa6\x9c5\xdf\x8c\x03UMU\xc1\x01\x86\x9dG"


# for i in range(len(pw1)):
#     pw1[i]+=1
#     pw1[i]=(~((pw1[i]^pw1[(i+1)%len(pw1)])+98))&0xff

from hashlib import sha256

for c in open('rockyou.txt', 'rb').readlines():
    c=c.replace(b'\n',b'')
    arr=list(c)
    for i in range(len(arr)):
        arr[i]+=1
        arr[i]=(~((arr[i]^arr[(i+1)%len(arr)])+98))&0xff
    res=bytes(arr)
    if sha256(res).digest()==target_hash:
        print(c)
        break
 ```

## Bogus

### 1. VPERMD

vpermd x1,x2,x3:  đem các phần tử từ mảng x3 sang x1 theo thứ tự được chỉ định trong x2

```python
def copyOrder(arr1, arr2):
    res=[]
    for i in range(len(arr1)):
        res.append(arr2[arr1[i]])
    return res
```

### 2. VPUNPCKLDQ

vpunpckhdq x1,x2,x3: mảng x1 chứa các phần tử của x2 và x3 theo quy tắc trên hình:

![image](https://user-images.githubusercontent.com/84214843/185082612-0ec1fb51-168a-476c-b50b-d4590baf088b.png)

```python
def mergeLow(arr1, arr2):
    res=[]
    pos=[0,1,4,5]
    for i in pos:
        res.append(arr1[i])
        res.append(arr2[i])
    return res
```

### 3. VPUNPCHLDQ

Tương tự như trên nhưng ở các vị trí còn lại.

```python
def mergeHigh(arr1, arr2):
    res=[]
    
    pos=[2,3,6,7]
    for i in pos:
        res.append(arr1[i])
        res.append(arr2[i])
    return res
```

### 4. vpcmpgtd: đọc code để hiểu

```python
def cmpGreater(arr1, arr2):
    res=[]
    for i in range(8):
        if arr1[i]>arr2[i]:
            res.append((-1)&0xf)
        else:
            res.append(0)
```

### 5. vpmovmskb: tương tự như u32 của pwntools

### Script để xem giá trị các thanh ghi xmm và ymm

```python
from pwn import u32
ymm0 = idaapi.regval_t()
ymm1 = idaapi.regval_t()
xmm1 = idaapi.regval_t()
xmm0 = idaapi.regval_t()
ymm6 = idaapi.regval_t()
ymm7 = idaapi.regval_t()
ymm2 = idaapi.regval_t()
ymm3 = idaapi.regval_t()
ymm12 = idaapi.regval_t()
idaapi.get_reg_val("ymm1", ymm1)
idaapi.get_reg_val("ymm0", ymm0)
idaapi.get_reg_val("xmm0", xmm0)
idaapi.get_reg_val("xmm1", xmm1)
idaapi.get_reg_val("ymm6", ymm6)
idaapi.get_reg_val("ymm7", ymm7)
idaapi.get_reg_val("ymm2", ymm2)
idaapi.get_reg_val("ymm3", ymm3)
idaapi.get_reg_val("ymm12", ymm12)
x0=[]
x1=[]
y0=[]
y1=[]
y6=[]
y7=[]
y2=[]
y3=[]
y12=[]
for i in range(0,len(xmm0.bytes()),4):
    x0.append(u32(xmm0.bytes()[i:i+4]))

for i in range(0,len(xmm1.bytes()),4):
    x1.append(u32(xmm1.bytes()[i:i+4]))

for i in range(0,len(ymm0.bytes()),4):
    y0.append(u32(ymm0.bytes()[i:i+4]))

for i in range(0,len(ymm1.bytes()),4):
    y1.append(u32(ymm1.bytes()[i:i+4]))

for i in range(0,len(ymm6.bytes()),4):
    y6.append(u32(ymm6.bytes()[i:i+4]))

for i in range(0,len(ymm7.bytes()),4):
    y7.append(u32(ymm7.bytes()[i:i+4]))

for i in range(0,len(ymm2.bytes()),4):
    y2.append(u32(ymm2.bytes()[i:i+4]))

for i in range(0,len(ymm3.bytes()),4):
    y3.append(u32(ymm3.bytes()[i:i+4]))

for i in range(0,len(ymm12.bytes()),4):
    y12.append(u32(ymm12.bytes()[i:i+4]))

print(f'{xmm0.bytes()} --> xmm0: {x0}')
print(f'{xmm1.bytes()} --> xmm1: {x1}')

print(f'{ymm0.bytes()} --> ymm0: {y0}')
print(f'{ymm1.bytes()}    --> ymm1: {y1}')
print(f'{ymm2.bytes()}    --> ymm2: {y2}')
print(f'{ymm3.bytes()} --> ymm3: {y3}')
print(f'{ymm6.bytes()} --> ymm6: {y6}')
print(f'{ymm7.bytes()} --> ymm7: {y7}')
print(f'{ymm12.bytes()} --> ymm12: {y12}')
print('----------------------------------------------------')
```

### Flow của chương trình:

```python
from pwn import u32

r8=0
data=[0]*0x1000
r11=0x246
inp=b'ABCDEFGHIJKLMNOP'
ymm0=list(inp[0:8])
ymm1=list(inp[8:16])

r8+=1
new_r11=0x10512156B2B05F6A
new_r11+=1
rax=new_r11

ebx=rax&0xffff
rax>>0x16
ebx<<=5
ymm6=data[ebx]

ebx=rax&0xffff
rax>>0x16
ebx<<=5
ymm7=data[ebx]

ebx=rax&0xffff
rax>>0x16
ebx<<=5
ymm10=data[ebx]

ebx=rax&0xffff
rax>>0x16
ebx<<=5
ymm11=data[ebx]

ymm0=copyOrder(ymm6, ymm0)
ymm1=copyOrder(ymm7, ymm1)

ymm2=mergeLow(ymm1,ymm0)
ymm3=mergeHigh(ymm1,ymm0)

ymm4=copyOrder(ymm10,ymm2)
ymm5=copyOrder(ymm11,ymm3)

ymm0=mergeLow(ymm5,ymm4)
ymm1=mergeHigh(ymm5,ymm4)

ymm12=[0,0,1,2,3,4,5,6]
ymm6=copyOrder(ymm12,ymm0)

ymm7=cmpGreater(ymm0,ymm6)
eax=u32(bytes(ymm7))
```


