import sys
input=sys.stdin.readline
INF=sys.maxsize

n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1): #반복문 상에서 k,a,b의 순서는 전혀 상관없음.
    for a in range(1,n+1):#반복문 순서가 달라지더라도 모든 경우를 다 계산하게 되고,
        for b in range(1,n+1): #최소값만 취하기 때문에 처리 순서(과정)는 달라도 결과는 같게됨.
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            #마찬가지로 패턴만 동일하다면 a,b,k가 서로 바뀌어도 문제없음.
#다만 k가 a와 b의 중간 노드라는 점에서 가장 바깥 for문에 위치하는게 가독성 측면에서 좋음.

for i in range(1,n+1):
    for j in range(1,n+1):
        if(graph[i][j]==INF):
            print("x",end=" ")
        else:
            print(graph[i][j],end=" ")
    print()



