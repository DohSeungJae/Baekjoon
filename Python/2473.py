import sys
input=sys.stdin.readline

N=int(input())
nList=list(map(int,input().split()))
nList.sort()

start=0
end=N-1
ans=[0,0,0]
absMin=sys.maxsize

for standard in range(N):
    num1=nList[standard]
    start,end=standard+1,N-1

    while start<end:
        num2,num3=nList[start],nList[end]
        sumOfSolution=num1+num2+num3

        if(abs(sumOfSolution)<absMin):
            absMin=abs(sumOfSolution)
            ans=[num1,num2,num3]
        
        if(sumOfSolution<0):
            start+=1
        else:
            end-=1

print(*ans)