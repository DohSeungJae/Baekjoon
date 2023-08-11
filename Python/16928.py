import sys
from collections import deque
input=sys.stdin.readline
board=[0 for i in range(101)]
cnts=[0 for i in range(101)]

def bfs(board,cnts,start):
    q=deque()
    q.append(start)
    
    while q:
        cur=q.popleft()
        for i in range(1,7):
            next=cur+i

            if(next>100 or cnts[next]):
                continue

            cnts[next]=cnts[cur]+1
            if(board[next]):
                if not cnts[board[next]]:
                    cnts[board[next]]=cnts[next]
                q.append(board[next])
                continue

                 
            q.append(next)

            
n,m=map(int,input().split()) # n : 사다리, m : 뱀
for _ in range(n+m):
    a,b=map(int,input().split())
    board[a]=b


bfs(board,cnts,1)

print(cnts[100])


#뱀/사다리를 만나면 무조건 이동
