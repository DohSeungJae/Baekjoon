import sys
input=sys.stdin.readline

score=[]
N=int(input())
for _ in range(N):
    score.append(int(input()))

reduced=0
for i in range(N-2,-1,-1):
    curScore=score[i]
    scoreLimit=score[i+1]
    if(curScore>=scoreLimit):
        reduced+=(curScore-scoreLimit+1)
        score[i]=score[i]-(curScore-scoreLimit+1)
    
print(reduced)

    