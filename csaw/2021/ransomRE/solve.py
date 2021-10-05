message1="us-aers-ransomware.pdf.backup"
message1_enc="a25981adfb782d04cccfb2ad66ae8e63ead31f62fb898913f1ec99359f2e1c4b.pdf.cryptastic"
flag_enc="ea6b505ffded681a256232ed214d4c3b410c8b4f052775eb7e67dcbd5af64e63.pdf.cryptastic"
f=open(message1,'rb').read()
f1=open(message1_enc,'rb').read()
f2=open(flag_enc,'rb').read()

data=[]
for i in range(len(f)):
    data.append(f[i] ^ f1[i])
data1=[]
for i in range(len(f2)):
    data1.append(data[i] ^ f2[i])

k=open('flag.pdf','wb')
k.write(bytes(data1))