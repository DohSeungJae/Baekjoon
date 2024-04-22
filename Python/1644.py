import sys
input=sys.stdin.readline

def sieveOfEratos(n:int)->list[int]:
    sieve=[1]*n
    m=int(n**0.5)

    for i in range(2,m+1):
        if(sieve[i]):
            for j in range(2*i,n,i):
                sieve[j]=0
    
    return [i for i in range(2,n) if (sieve[i])]

N=int(input())
primeList=sieveOfEratos(N+1)

start=0
end=1
cnt=0
while(end<=len(primeList) and start<=end):
    partSum=sum(primeList[start:end])
    if(partSum==N):
        cnt+=1
        end+=1
    elif(partSum<N):
        end+=1
    else:
        start+=1

print(cnt)
