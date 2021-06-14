from Crypto.Util.number import long_to_bytes

with open('wtflag_enc', 'rb') as f:
    data=f.read()

data1,data2=data.split(b'SSSS')

out1=int(data1.hex()[:-1],16)       #vì mình nhận thấy sau khi tách ra thì có một số 0 ở cuối do chương trình
                                    #thêm vào
out2=int(data2.hex(),16)

#(v17+2*v16)/3=out1
#(v16+ 2*2*v17)/3=out2

v17=(6*out2-3*out1)//7
v16=(12*out1-3*out2)//7

for i in range(v17-100,v17+100):
    for j in range(v16-100, v16+100):
        res=str(i)+ str(j)
        if b'S4CTF{' in long_to_bytes(res):
            print(long_to_bytes(res).decode())