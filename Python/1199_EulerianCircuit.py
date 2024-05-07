import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**9)

class EulerianGraph:
    def __init__(self,vertex):
        self.v=vertex
        self.graph={i:{} for i in range(self.v)}
       
    def addEdge(self,a,b,w):
        if(w==0):
            return 
        self.graph[a][b]=w
    
    def getEulerianCircuit(self,c):
        while self.graph[c]:
            n,cnt=self.graph[c].popitem()
            if(cnt>1):
                self.graph[c][n]=cnt-1
            
            if(self.graph[n][c]>1):
                self.graph[n][c]-=1
            else:
                del self.graph[n][c]

            self.getEulerianCircuit(n)
        print(c+1,end=" ")

N=int(input())
g=EulerianGraph(N)
doesExist=1
for i in range(N):
    line=list(map(int,input().split()))
    for j in range(N):
        g.addEdge(i,j,line[j])
    if(sum(line)%2==1):
        doesExist=0

if(not doesExist):
    print(-1)
    exit(0)

g.getEulerianCircuit(0)