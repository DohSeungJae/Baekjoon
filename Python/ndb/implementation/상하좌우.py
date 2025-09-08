import sys
input=sys.stdin.readline

directions=["L","R","U","D"]
nextYX=[[0,-1],[0,1],[-1,0],[1,0]]
y,x=1,1

N=int(input())
commands=input().split()
for c in commands:
    for i in range(4):
        if(directions[i]==c):
            dy=nextYX[i][0]
            dx=nextYX[i][1]
    
    if(y+dy>N or y+dy<1):
        continue
    if(x+dx>N or x+dx<1):
        continue
    
    y=y+dy
    x=x+dx

print(x,y)
