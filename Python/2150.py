from collections import defaultdict,deque
import sys
input=sys.stdin.readline

class SCC:
    def __init__(self,vertex):
        self.v=vertex
        self.graph=[[] for _ in range(self.v)]

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def SCCdfs(self,v):
        global id
        id+=1
        d[v]=id
        s.append(v)

        parent=d[v]
        for i in range(len(self.graph[v])):
            j=self.graph[v][i]
            if(d[j]==0):
                parent=min(parent, self.SCCdfs(j))
            elif(not finished[j]):
                parent=min(parent,d[j])


        if(parent==d[v]):
            scc=deque()
            while True:
                t=s.pop()

                scc.appendleft(t)
                finished[t]=True
                if(t==v):
                    break
        
            totalScc.append(scc)

        return parent


if __name__=="__main__":

    MAX=10001
    d=[0]*MAX
    id=0
    s=[]
    finished=[False]*MAX
    totalScc=[]
    sccList=[]
    n,m=map(int,input().split())
    gr=SCC(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        gr.addEdge(a,b)
    
    for i in range(n):
        if(d[i]==0):
            gr.SCCdfs(i)

    for i in totalScc[1:]:
        sccList.append(sorted(i))

    print(len(sccList))

    for i in sorted(sccList):
        for j in i:
            print(j,end=" ")
            
        print(-1)


    



        