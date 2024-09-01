import sys
input=sys.stdin.readline

N,M=map(int,input().split())
packMinCost,eachMinCost=sys.maxsize,sys.maxsize

for _ in range(M):
    packCost,eachCost=map(int,input().split())
    packMinCost=min(packMinCost,packCost)
    eachMinCost=min(eachMinCost,eachCost)
    
if(eachMinCost <= packMinCost/6):
    print(N*eachMinCost)
    exit(0)
onlyPack,packAndEach=sys.maxsize,sys.maxsize

if(N%6!=0):
    onlyPack=((N//6)+1)*packMinCost
    packAndEach=(N//6)*packMinCost+(N%6)*eachMinCost
    print(min(onlyPack,packAndEach))
else:
    onlyPack=(N//6)*packMinCost
    print(onlyPack)