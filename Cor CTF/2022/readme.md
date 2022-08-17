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

### 2. VPUNPCKLDQ

vpunpckhdq x1,x2,x3: mảng x1 chứa các phần tử của x2 và x3 theo quy tắc trên hình:

![image](https://user-images.githubusercontent.com/84214843/185082612-0ec1fb51-168a-476c-b50b-d4590baf088b.png)

### 3. VPUNPCHLDQ

Tương tự như trên nhưng ở các vị trí còn lại.

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


