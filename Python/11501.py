import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    cost=list(map(int,input().split()))
    costReversed=cost[::-1]
    profitSum=0

    std=costReversed[0]
    for i in range(1,N):
        diff=std-costReversed[i]
        if(diff>0):
            profitSum+=diff
        else:
            std=costReversed[i]

    print(profitSum)