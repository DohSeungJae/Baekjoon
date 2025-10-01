import sys
input=sys.stdin.readline

def find_parent(parent,x):
    if(parent[x]!=x):
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if(a<b):
        parent[b]=a
    else:
        parent[a]=b


n,m=map(int,input().split())
edges=[]
parent=[i for i in range(n+1)]

for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort() ##!!


summ=0
max_cost=0
for (cost,a,b) in edges:
    if(find_parent(parent,a)==find_parent(parent,b)):
        continue
    union_parent(parent,a,b)
    summ+=cost
    max_cost=max(max_cost,cost)
    # 비용이 작은 간선부터 순서대로 순회하기 때문에
    # max 함수를 사용할 필요가 없음.

summ-=max_cost
print(summ)