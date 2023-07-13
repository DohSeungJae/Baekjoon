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
            diff=block[i][j]-h #양수이면 block이 더 높음, 음수이면 기준 높이(h)가 더 높음
            
            if(diff>0): #현재 block이 더 높을 때 > 내려가야함. 인벤토리 공간.
                inven+=diff
                down+=diff
                
            else: ##현재 block이 더 낮을 때 > 올라가야함. /혹은 기준높이와 현재높이가 같을때 
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

    

