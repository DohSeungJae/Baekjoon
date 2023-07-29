import sys
input=sys.stdin.readline

n=int(input())
stairs=[]
for _ in range(n):
    stairs.append(int(input()))

stairs=stairs[::-1]
res=[]

if(n==1):
    print(stairs[-1])
elif(n==2):
    print(stairs[-1]+stairs[-2])
elif(n==3):
    res=[0,stairs[0],stairs[0]+stairs[1],stairs[0]+stairs[2]]
    res.append(max(res[n-2]+stairs[n-1],res[n-3]+stairs[n-3]+stairs[n-1]))
    print(max(res))

else:

    res=[0,stairs[0],stairs[0]+stairs[1],stairs[0]+stairs[2]]
    for i in range(4,n+1):
        maxi=max(res[i-2]+stairs[i-1],res[i-3]+stairs[i-2]+stairs[i-1])
        res.append(maxi)


    print(max(res))
    

