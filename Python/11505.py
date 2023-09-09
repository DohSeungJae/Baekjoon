import sys
input=sys.stdin.readline
module=1000000007

class SegmentTree_multiple:
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
        self.tree[node]=(self.tree[2*node]*self.tree[2*node+1])%module
    
    def query_multiple(self,ql,qr,node,left,right):
        if left > qr or right < ql:
            return 1
        
        if(ql<=left and right<=qr):
            return self.tree[node] 
        
        mid=(left+right)//2
        left_sum=self.query_multiple(ql,qr,2*node,left,mid)
        right_sum=self.query_multiple(ql,qr,2*node+1,mid+1,right)
        return (left_sum*right_sum)%module
    
    def update(self,idx,value,node,left,right):
        if left==right:
            self.tree[node]=value
            return 
        
        mid=(left+right)//2
        if(left<=idx<=mid):
            self.update(idx,value,node*2,left,mid)
        else:
            self.update(idx,value,node*2+1,mid+1,right)

        self.tree[node]=(self.tree[2*node]*self.tree[2*node+1])%module

if __name__=="__main__":
    arr=[]
    n,m,k=map(int,input().split())

    for _ in range(n):
        arr.append(int(input()))
    seg_tree_multi=SegmentTree_multiple(arr)

    for _ in range(m+k):
        a,b,c=map(int,input().split())
        if a==1: #modi
            seg_tree_multi.update(b-1,c,1,0,len(arr)-1)
        else:
            if(b>c):
                b,c=c,b
            print(seg_tree_multi.query_multiple(b-1,c-1,1,0,len(arr)-1)%module)


