import sys
input=sys.stdin.readline

class SegmentTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.tree=[0] * (4*self.n) #?
        self.lazy=[0] * (4*self.n)
        self.build(1,0,self.n-1,arr)
    
    def build(self,node,left,right,arr):
        if(left==right):
            self.tree[node]=arr[left]
            return 

        mid=(left+right)//2
        self.build(2*node,left,mid,arr)
        self.build(2*node+1,mid+1,right,arr)
        self.tree[node]=self.tree[2*node]+self.tree[2*node+1]
    
    def query(self,ql,qr,node,left,right):
        if left > qr or right < ql:
            return 0
        
        if(ql<=left and right<=qr):
            return self.tree[node] 
        
        mid=(left+right)//2
        left_sum=self.query(ql,qr,2*node,left,mid)
        right_sum=self.query(ql,qr,2*node+1,mid+1,right)
        return left_sum+right_sum
    
    def update(self,node,idx,value,left,right):
        if left==right:
            self.tree[node]=value
            return 
        
        mid=(left+right)//2
        if(left<=idx<=mid):
            self.update(2*node,idx,value,left,mid)
        else:
            self.update(2*node+1,idx,value,mid+1,right)
        
        self.tree[node]=self.tree[2*node]+self.tree[2*node+1]

if __name__=="__main__":
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))

    seg_tree=SegmentTree(arr)

    for _ in range(q):
        x,y,a,b=map(int,input().split())
        if(x>y):
            x,y=y,x
        print(seg_tree.query(x-1,y-1,1,0,len(arr)-1))
        seg_tree.update(1,a-1,b,0,len(arr)-1)

