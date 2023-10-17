table=[]
maxLen=0
for _ in range(5):
    temp=str(input())
    maxLen=max(maxLen,len(temp))
    table.append(temp)

for idx in range(maxLen):
    for line in range(5):
        curLen=len(table[line])
        if idx>curLen-1:
            continue
        print(table[line][idx],end="")


