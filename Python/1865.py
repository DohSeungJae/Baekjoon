import sys
input=sys.stdin.readline
INF=sys.maxsize

def bf()->bool:
    #start=1
    #minCost[start]=0

    for i in range(N):
        for j in range(2*M+W):
            curNode,nextNode,cost=arr[j]
            if( minCost[nextNode]>minCost[curNode]+cost):
                minCost[nextNode]=minCost[curNode]+cost
                if(i==N-1):
                    return True
    return False
    

TC=int(input())
for _ in range(TC):
    N,M,W=map(int,input().split())
    arr=[]
    minCost=[INF for _ in range(N+1)]

    for _ in range(M):
        S,E,T=map(int,input().split())
        arr.append((S,E,T))
        arr.append((E,S,T))

    for _ in range(W):
        S,E,T=map(int,input().split())
        arr.append((S,E,-T))
    
    '''
    for i in range(M+W):
        S,E,T=map(int,input().split())
        if(i>=M):
            T=-T
        else:
            arr.append((E,S,T))
        arr.append((S,E,T))
    '''
    isNegativeCycle=bf()
    if(isNegativeCycle):
        print("YES")
    else:
        print("NO")
        
        

        