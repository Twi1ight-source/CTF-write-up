f=open('dump','rb').read()

arr=[]
end=f.find(b'\x03')
f=f[:end+1]
arr_1=[]
for i in range(len(f)):
    arr.append(f[i])
for i in range(len(arr)):
    if arr[i]!=0:
        arr_1.append(i)
print(arr_1)
