import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())
heights=set()
block=[]

for _ in range(n):
    temp=list(map(int,input().split()))
    block.append(temp)

res=sys.maxsize
idx=0
for h in range(257):
    inven=b
    time=0
    up=0
    down=0

    for i in range(n):
        for j in range(m):
            diff=block[i][j]-h 
            
            if(diff>0): 
                inven+=diff
                down+=diff
                
            else: 
                diff=-1*diff
                inven-=diff
                up+=diff

    if(inven<0):
        continue

    time=up+2*down

    if(time<=res):
        
        res=time
        idx=h

print(res,idx)

    

