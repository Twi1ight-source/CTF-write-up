a=[
[1, 13],
[1, 14],
[1, 15],
[2, 15],
[3, 15],
[3, 14],
[3, 13],
[3, 12],
[3, 11],
[4, 11],
[5, 11],
[6, 11],
[7, 11],
[7, 10],
[7, 9],
[7, 8],
[7, 7],
[6, 7],
[5, 7],
[5, 6],
[5, 5],
[5, 4],
[5, 3],
[5, 2],
[5, 1],
[6, 1],
[7, 1],
[7, 2],
[7, 3],
[8, 3],
[9, 3],
[10, 3],
[11, 3],
[12, 3],
[13, 3],
[13, 2],
[13, 1],
[14, 1],
[15, 1],
[15, 2],
[15, 3],
[16, 3],
[17, 3],
[17, 4],
[17, 5],
[16, 5],
[15, 5],
[15, 6],
[15, 7],
[15, 8],
[15, 9],
[15, 10],
[15, 11],
[14, 11],
[13, 11],
[13, 10],
[13, 9],
[12, 9],
[11, 9],
[11, 10],
[11, 11],
[11, 12],
[11, 13],
[11, 14],
[11, 15],
[12, 15],
[13, 15],
[13, 16],
[13, 17],
[12, 17],
[11, 17],
[11, 18],
[11, 19],
[12, 19],
[13, 19],
[13, 20],
[13, 21],
[12, 21],
[11, 21],
[11, 22],
[11, 23],
[12, 23],
[13, 23],
[14, 23],
[15, 23],
[15, 22],
[15, 21],
[15, 20],
[15, 19],
[16, 19],
[17, 19],
[18, 19],
[19, 19],
[19, 20],
[19, 21],
[20, 21],
[21, 21],
[22, 21],
[23, 21],
[23, 20],
[23, 19],
[24,19]
]
arr=""
for i in range(len(a)-1):
    if a[i][0]==a[i+1][0]:
        if a[i][1] < a[i+1][1]:
            arr+="l"
        else:
            arr+='h'
    else:
        if a[i][0]<a[i+1][0]:
            arr+='k'
        else:
            arr+='j'
print(arr)
