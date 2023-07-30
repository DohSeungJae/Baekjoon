import sys
import math
input=sys.stdin.readline

n=int(input())

sq=[0,1,2,3,1]
if(n<5):
    print(sq[n])
    exit(0)

for i in range(5,n+1):
    root=math.sqrt(i)
    if(root==int(root)):
        sq.append(1)
    else:
        temp=[]
        maxSq=1
        while maxSq**2<=i:
            
            cand=sq[maxSq**2]+sq[i-maxSq**2]
            temp.append(cand)
            maxSq+=1

        sq.append(min(temp))

print(sq[n])

        
##Pypy3
#Four Squares