import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    p,c,w=map(int,input().split())
    tree[p].append((c,w))

stackA=[0]
maxDiameter=0 

def backTracking(curNode:int,weight:int)->None:
    print(curNode)
    
    global maxDiameter
    if(tree[curNode]==[]): #이 조건문은 필요없는 것 같다
        return weight #가중치를 return해서 상위 함수에서 합산하도록 처리
    stack=[] #자식들의 가중치 값을 저장한 스택 
    for child in tree[curNode]:
        stack.append(backTracking(child[0],child[1]))
        #상위 함수로 lineWeight를 반환해야함.
    if(len(stack)>=2):
        stack.sort(reverse=True)
        maxDiameter=max(stack[0]+stack[1],stack[0]+weight)
    if(maxDiameter>stackA[-1]):
        stackA.append(maxDiameter)
    return weight+stack[0]


backTracking(1,0)
print(stackA)
print(maxDiameter)

#backTracking함수의 시작(루트)노드는 1
#backTracking(1,0,0,[])


    
