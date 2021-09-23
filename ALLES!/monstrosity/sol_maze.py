import struct
TOP = 1
RIGHT = 2 
BOTTOM = 4
LEFT = 8

token=[[i for i in range(10)] for k in range(10)]
for i in range(10):
    for j in range(10):
        token[i][j]=0x10+ 10*j + i

char_set='abcdefghijklmnopqrstuvwxyz'
def get_code(token):
    code=[0]*4
    code[0]=ord(char_set[(token +13)%0x1A])  #w
    code[1]=ord(char_set[(token +43)%0x1A])  #a
    code[2]=ord(char_set[(token +57)%0x1A])  #s
    code[3]=ord(char_set[(token +24)%0x1A])  #d
    return code


maze = [[i for i in range(10)] for k in range(10)]
with open("maze.bin", "rb") as f:
    for x in range(10):
        for y in range(10):
            maze[x][y] = struct.unpack("<I", f.read(4))[0]

def maze_walk(maze, x0, y0):
    visited = [[0 for i in range(10)] for k in range(10)]
    queue = []
    queue.append([(x0,y0)])
    while (len(queue) != 0):
        path = queue.pop(0)
        (x,y) = path[-1]
        visited[x][y] = True
        if (x == 9 and y == 9):
            return path
        status = maze[x][y]
        neighbor = []
        if not (status & TOP) and y > 0:
            neighbor.append((x, y -1))
        if (not (status & BOTTOM) and y < 9):
            neighbor.append((x, y + 1))
        if (not (status & LEFT) and x > 0):
            neighbor.append((x - 1, y))
        if (not (status & RIGHT) and x < 9):
            neighbor.append((x + 1, y))
        #print(neighbor)
        new_path = [path + [(x,y)] for (x,y) in neighbor if not visited[x][y]]
        queue += new_path
    print("WRONG")

sol=maze_walk(maze,0,0)
print(sol)
flag=""
for i in range(len(sol)-1):
    (x,y)=sol[i]
    (x1,y1)=sol[i+1]
    code=get_code(token[x][y])

    if x1<x:  #left
        flag+=chr(code[1])
    if x1>x: #right
        flag+=chr(code[3])
    if y1<y: #top
        flag+=chr(code[0])
    if y1>y: #bot
        flag+=chr(code[2])

print(flag)



