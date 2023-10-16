import sys
input=sys.stdin.readline

n,l=map(int,input().split())

x=list(map(int,input().split()))
w=list(map(int,input().split()))

start=1
end=l

while start<=end:
    mid=((start+end)/2)
    w_l=0
    w_r=0
    
    for i in range(n):
        v=abs(mid-x[i])*w[i]
        if(x[i]<mid):
            w_l+=v
        else:
            w_r+=v
        
    if(w_l>w_r):
        mid=start+1
    elif(w_l<w_r):
        mid=end-1
    
    elif(w_l==w_r):
        break

    print(end)
    



    
print(end)



    
