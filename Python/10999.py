import sys
input=sys.stdin.readline

class LazySegmentTree:
    def __init__(self, arr):
        self.n =len(arr)
        self.tree=[0]*(4*self.n)
        self.lazy=[0]*(4*self.n)
        self.build(1,0,self.n-1,arr)

    def build(self,node,left,right,arr):
        if left==right:
            self.tree[node]=arr[left]
            return

        mid=(left+right)//2
        self.build(2*node,left,mid,arr)
        self.build(2*node+1,mid+1,right,arr)
        self.tree[node]=self.tree[2*node]+self.tree[2*node+1]

    def propagate(self,node,left,right):
        if self.lazy[node]!=0:
            self.tree[node]+=self.lazy[node]*(right-left+1)
            if left!=right:
                self.lazy[2*node]+=self.lazy[node]
                self.lazy[2*node+1]+=self.lazy[node]
            self.lazy[node]=0

    def update(self,ql,qr,value,node,left,right):
        self.propagate(node,left,right)

        if left>qr or right<ql:
            return

        if ql<=left and right<=qr:
            self.lazy[node]+=value
            self.propagate(node,left,right)
            return

        mid=(left+right)//2
        self.update(ql,qr,value,2*node,left,mid)
        self.update(ql,qr,value,2*node+1,mid+1,right)
        self.tree[node]=self.tree[2*node]+self.tree[2*node+1]

    def query(self,ql,qr,node,left,right):
        self.propagate(node,left,right)

        if left>qr or right<ql:
            return 0

        if ql<=left and right<=qr:
            return self.tree[node]

        mid=(left+right)//2
        left_sum=self.query(ql,qr,2*node,left,mid)
        right_sum = self.query(ql,qr,2*node+1,mid+1,right)
        return left_sum+right_sum
    

if __name__=="__main__":
    n,m,k=map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    lazySegTree=LazySegmentTree(arr)
    
    for _ in range(m+k):
        cmdLine=list(map(int,input().split()))
        if(cmdLine[0]==1): #modify
            b,c,d=cmdLine[1],cmdLine[2],cmdLine[3]
            lazySegTree.update(b-1,c-1,d,1,0,len(arr)-1)

        else:
            b,c=cmdLine[1],cmdLine[2]
            print(lazySegTree.query(b-1,c-1,1,0,len(arr)-1))
