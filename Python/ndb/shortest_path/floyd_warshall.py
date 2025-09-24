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
#플로이드 워셜 알고리즘은 두 노드의 거리와 그 사이의 거쳐가는 노드를 통한 거리를 비교해 최단거리를 계산함.
#거쳐가는 중간 노드 기준으로 알고리즘이 수행되기 때문에
#중간 노드인 k가 가장 바깥 for문에 위치하는 것이 가독성 측면에서 좋음. 

for i in range(1,n+1):
    for j in range(1,n+1):
        if(graph[i][j]==INF):
            print("x",end=" ")
        else:
            print(graph[i][j],end=" ")
    print()



