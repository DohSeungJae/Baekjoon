import sys
input=sys.stdin.readline
N,S=map(int,input().split())
sequence=list(map(int,input().split()))

stack=[]
cnt=0
def bt(start:int,summary:int)->None:
    global cnt
    if(start>0 and summary==S):
        cnt+=1 

    for i in range(start,N):
        summary+=sequence[i]
        bt(i+1,summary)
        summary-=sequence[i]

bt(0,0)
print(cnt)