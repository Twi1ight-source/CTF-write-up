import numpy as np

r = open('93839392490432','rb').read()     #input 
q = np.frombuffer(r, dtype=np.float32)
inp = np.matrix(np.reshape(q, (8, 8)).astype(np.float32))

f = open('output.txt','rb').read()	   #output
q1 = np.frombuffer(f, dtype=np.float32)
out = np.matrix(np.reshape(q1, (8, 8)).astype(np.float32))

#print(O)

#print(O1)

res=np.dot(inp,inp)
for i in range(5):
    res=np.dot(res,inp)

inv=np.linalg.inv(res.transpose())
print(np.dot(out,inv))



    

