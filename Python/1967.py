import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    p,c,w=map(int,input().split())
    tree[p].append((c,w))

maxDiameter=0 
def backTracking(curNode:int,weight:int,lineWeight:int)->None:
    global maxDiameter
    if(tree[curNode]==[]):
        return weight 

    stack=[] 
    for child in tree[curNode]:
        stack.append(backTracking(child[0],child[1],lineWeight))
    stack.sort(reverse=True)
    lineWeight+=stack[0]
    maxDiameter=max(maxDiameter,lineWeight)
    if(len(stack)>=2):
        maxDiameter=max(maxDiameter,stack[0]+stack[1])    
    return lineWeight+weight

backTracking(1,0,0)
print(maxDiameter)
