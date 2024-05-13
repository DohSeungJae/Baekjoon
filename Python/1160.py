import sys
input=sys.stdin.readline

m,a,c,x0,n,g=map(int,input().split())
x=[x0]
nums=set()
prevLen=len(nums)
while True:
    newX=(a*x[-1]+c)%m
    nums.add(newX)
    if(prevLen==len(nums)):
        break
    prevLen=len(nums)
    x.append(newX)

interval=prevLen
xn=x[n%interval]
print(xn%g)


