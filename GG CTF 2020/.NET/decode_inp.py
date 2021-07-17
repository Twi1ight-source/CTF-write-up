a=[12,29,15,62,12,51,51,12,47,53,18,54,32,40,44,53,39,11,56,55,27,40,36,47,47,60,15,56,49,63]

flag=""
for i in a:
    if i==63:
        i=125
        flag+=chr(i)
    elif i==62:
        i=123
        flag+=chr(i)
    elif i in range(10,36):
        i+=55
        flag+=chr(i)
    elif i in range(36,62):
        i+=61
        flag+=chr(i)
    elif i in range(0,10):
        i=i
        flag+=str(i)
print(flag)

