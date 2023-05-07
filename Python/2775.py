import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    p=[]
    k=int(input()) #층
    n=int(input()) #호
    
    for i in range(n+(n*k)):
        if(i<n): p.append(i+1)
        elif(i%n==0): p.append(1)
        else: p.append(p[i-1]+p[i-n])

    print(p[-1])




    




