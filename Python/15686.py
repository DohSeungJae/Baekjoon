import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[]
cordinateOf2=[]
cordinateOf1=[]

for y in range(N):
    line=list(map(int,input().split()))
    if 2 in line:
        for x in range(len(line)):
            if(line[x]==2):
                cordinateOf2.append((y,x))
    if 1 in line:
        for x in range(len(line)):
            if(line[x]==1):
                cordinateOf1.append((y,x))
    graph.append(line)

minDist=sys.maxsize
stack=[]
cntOf2=len(cordinateOf2)
cnt=0

def remove2(start:int):
    condition=cntOf2-len(stack)
    if(M==condition):
        calculateDistance(stack)
        return 
    for i in range(start,len(cordinateOf2)):
        (y,x)=cordinateOf2[i]
        if((y,x) not in stack):
            stack.append((y,x))
            remove2(i+1)
            stack.pop()

def calculateDistance(stack:list)->None:
    global minDist
    distance={}
    for fr in cordinateOf2:
        if(fr in stack):
            continue
        for to in cordinateOf1:
            if(to not in distance.keys()):
                distance[to]=sys.maxsize
            distance[to]=min(distance[to],abs(fr[0]-to[0])+abs(fr[1]-to[1]))
    sumOfDistances=0
    for i in distance.keys():
        sumOfDistances+=distance[i]
    minDist=min(minDist,sumOfDistances)

remove2(0)
print(minDist)
