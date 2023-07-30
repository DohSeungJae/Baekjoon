import sys
input=sys.stdin.readline

n=int(input())

sq=[0,1,2,3,1]
if(n<5):
    print(sq[n])
    exit(0)

for i in range(5,n+1):
    root=int(i**0.5)
    if(root*root==i):
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