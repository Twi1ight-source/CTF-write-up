from z3 import *
s=Solver()

inp=[BitVec(f'{i}',8) for i in range(10)]

arr=Array('arr',BitVecSort(8),BitVecSort(8))        #tạo mảng arr với các phần tử 8 bits

for i in range(10):
    arr=Store(arr,i,0)

for i in range(10):
    s.add(9>=inp[i]-48)
    arr=Store(arr,inp[i]-48,arr[inp[i]-48]+1)

for i in range(10):
    s.add(arr[i]==inp[i]-48)

print(s.check())
if s.check()==sat:
    m=s.model()
    for i in inp:
        print(chr(m[i].as_long()),end="")

