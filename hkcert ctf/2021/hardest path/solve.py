f=open('out.txt', 'r').read().strip()

import re
dic={}
f=f.split("\n")
for i in f:
    left ,right= i.split(' = ')
    if right == '_29aa7a86665899ed':
        dic[left]=[]
    else:
        func=re.findall(r'_[0-9a-f]{1,16}', right)[1:]
        dic[left]=func

src='_328518a497015157'
dest='_8b0eb6f195ae182a'

queue=[]
visited=set()
queue.append((src, ''))

while len(queue) > 0:
    first, path= queue[0]
    if first == dest:
        print(path)
    visited.add(first)
    for id in range(len(dic[first])):  #4 options
        reachable= dic[first][id]
        if reachable not in visited:
            char='NEWS'[id]
            queue.append((reachable, path+char))
    del queue[0]

    