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
    
v,e=map(int,input().split())

parent=[i for i in range(v+1)]
edges=[]
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()


summ=0
for (cost,a,b) in edges:
    if(find_parent(parent,a)==find_parent(parent, b)): #사이클 생성
        continue
    union_parent(parent,a,b)
    summ+=cost


print(summ)



