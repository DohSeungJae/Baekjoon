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

            if(next>100):
                continue

            if(board[next]!=0):
                if(cnts[board[next]]==0):

                    cnts[board[next]]=cnts[next]
                    cnts[next]=cnts[cur]+1
                    q.append(next)
                    q.append(board[next])
                
                else: #이미 방문했을 때
                    cnts[next]=cnts[cur]+1
                    
                    

                    
            else:
                if(cnts[next]==0):
                    print(cur,next)
                    
                    cnts[next]=cnts[cur]+1
                    q.append(next)

                               
n,m=map(int,input().split()) # n : 사다리, m : 뱀
for _ in range(n+m):
    a,b=map(int,input().split())
    board[a]=b


bfs(board,cnts,1)

print(cnts)
print(board)



