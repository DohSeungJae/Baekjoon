n,k=map(int,input().split())
lst=[[0 for _ in range(7)] for _ in range(2)]

for _ in range(n):
    s,y=map(int,input().split())
    lst[s][y]+=1

cnt=0
for s in range(2):
    for y in range(1,7):
        if(lst[s][y]==0):
            continue
        cnt=cnt+((lst[s][y]-1)//k)+1

print(cnt)
