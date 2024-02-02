import sys
input=sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]
parentOf={}
leaves=[]

for _ in range(n-1):
    p,c,w=map(int,input().split())
    tree[p].append((c,w))
for i in range(1,n+1):
    if(tree[i]==[]):
        leaves.append(i)

stack=[]
maxDiameter=0 

def backTracking(curNode:int,line1:int,line2:int)->None:
    global maxDiameter
    if(tree[curNode]==[]):
        return 
    for child in tree[curNode]:
        stack.append(child[0])
        backTracking(tree,child[0])
        stack.pop()

        
print(tree)
#backTracking함수의 시작(루트)노드는 1


    
