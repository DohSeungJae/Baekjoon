import sys
input=sys.stdin.readline

table=[]
maxi=0
idx=[0,0]
for _ in range(9):
    table.append(list(map(int,input().split())))

for y in range(9):
    for x in range(9):
        if table[y][x]>maxi:
            maxi=table[y][x]
            idx=[x,y]
        
print(maxi)
print(idx[1]+1,idx[0]+1)

#변수를 선언하지 않고 사용하면 nameError가 발생할 수 있음.
