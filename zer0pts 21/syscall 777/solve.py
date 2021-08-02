from z3 import *
s=Solver()
check=[
    [4127179254,4126139894,665780030,666819390],
    [1933881070,2002783966,1601724370,1532821474],
    [4255576062,3116543486,3151668710,4290701286],
    [1670347938,4056898606,2583645294,197094626],
    [2720551936,1627051272,1627379644,2720880308],
    [2307981054,3415533530,3281895882,2174343406],
    [2673307092,251771212,251771212,2673307092],
    [4139379682,3602496994,3606265306,4143147994],
    [4192373742,4088827598,3015552726,3119098870],
    [530288564,530288564,3917315412,3917315412],
    [4025255646,2813168974,614968622,1827055294],
    [3747612986,1340672294,1301225350,3708166042],
    [3098492862,3064954302,3086875838,3120414398],
    [2130820044,2115580844,2130523044,2145762244]
]


inp=[BitVec(f'inp{i}',32) for i in range(15)]

mem=[0]*12
def solve():
    for i in range(15):
        args=[0]*4
        args[0]=inp[i]
        args[1]=inp[(i+1)%14]
        args[2]=inp[(i+2)%14]
        args[3]=inp[(i+3)%14]

        s.add(args[0]&0xff <128)
        s.add((args[0]>>8)&0xff <128)
        s.add((args[0]>>16)&0xff <128)
        s.add((args[0]>>24)&0xff <128)

        mem[0]=args[0]
        mem[1]=args[1]^mem[0]
        mem[2]=args[2]^mem[1]
        mem[3]=args[3]^mem[2]

        mem[4]=mem[0]+mem[1]+mem[2]+mem[3]
        mem[5]=mem[0]-mem[1]+mem[2]-mem[3]
        mem[6]=mem[0]+mem[1]-mem[2]-mem[3]
        mem[7]=mem[0]-mem[1]-mem[2]+mem[3]

        mem[8]=(mem[6]&mem[7]) ^(mem[4]|mem[5])
        mem[9]=(mem[7]&mem[4]) ^ (mem[5] | mem[6])
        mem[10]=(mem[4]&mem[5]) ^ (mem[6] | mem[7])
        mem[11]=(mem[5]&mem[6]) ^(mem[7] | mem[4])

        s.add(Or(*[And(mem[8] == val[0], mem[9] == val[1], mem[10] == val[2], mem[11] == val[3]) for val in check]))

solve()
s.add(inp[0] ==0x3072657a)
s.add(inp[1] ==0x7b737470)

print(s.check())
if s.check()==sat:
    print(s.model())

