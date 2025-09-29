
def find_parent_uncompressed(parent,x): #경로 압축을 적용하지 않은 코드
    if(parent[x]!=x):
        return find_parent_uncompressed(parent,parent[x])
    return x

def find_parent(parent,x): #경로 압축을 적용한 코드
    if(parent[x]!=x):
        parent[x]=find_parent(parent,parent[x]) #경로 압축을 하지 않았을 때의 return값과
        #동일한 값을 parent[x]에 저장해 부모 테이블 값을 갱신함.
        #다음번 find 연산 때 반복 재귀 없이 바로 root값을 찾을 수 있음. <- 시간 복잡도 최적화

    return parent[x] #if문에서 return을 하지 않은 대신에 그것과 같은 값을 return함.
    #if문에 걸리지 않았다면 x와 parent[x]는 같은 값이기 때문에 결과는 같음.

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[i for i in range(v+1)] 
#parent 리스트를 선언할 때 주의, 노드 번호로 indexing 하기 때문에 리스트의 크기는 (v+1)이여야함.  

for _ in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

for i in range(1,v+1):
    find_parent(parent,i)

print(*parent)

