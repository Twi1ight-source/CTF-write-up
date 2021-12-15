
var_0= 68694329 
def w():
    global var_0
    var_0 *= 1259409 
    var_0+=321625345 
    var_0 %=4294967296 

    return var_0

def init(n):
    a=[]
    var_1=0
    while var_1<n:
        a.append(w())
        var_1+=1
    return a

def s(x,y):
    
    var_2=a[x]
    a[x]=a[y]
    a[y]=var_2


def r(x,y):
    if x>y:
        return r(y,x)
    while x<y:
        s(x,y)
        x+=1
        y-=1
    
def o(x,y,val):
    if x>y:
        return o(y,x,val)
    var_3=x
    while var_3<=y:
        a[var_3] ^= val
        var_3+=1

var_7=200000
var_9=0

a=init(var_7)

while var_9 < var_7*5:
    var_10= w()%3
    var_11= w()% var_7
    var_12= w()% var_7

    if var_12 ==0:
        r(var_11,var_12)

    if var_12 ==1:
        s(var_11, var_12)
    
    if var_12 ==2:
        var_13=w()
        o( var_11, var_12, var_13)
    
    var_9+=1

print(a)
i=0
sum=0
while i <200000:
    sum+=a[i] * (i+1)
    i+=1

print('hitcon{'+str(sum) + '}')




