import sys
input=sys.stdin.readline

n=int(input())
cord=[[-1,-1]]

def dot(cord,n):
    res=0
    for i in range(1,n):
        res+=cord[i][0]*cord[i+1][1]
        res-=cord[i+1][0]*cord[i][1]
    
    return abs(res)

for _ in range(n):
    cord.append(list(map(int,input().split())))
cord.append([cord[1][0],cord[1][1]])

print(f"{0.5*dot(cord,n):.1f}")
print(cord)


