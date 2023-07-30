import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    d={}

    for __ in range(n):
        name,cate=map(str,(input().strip()).split())
        if cate in d.keys():
            d[cate]+=1
        else:
            d[cate]=1

    cnt=1
    for k in d.keys():
        cnt*=d[k]+1
    
    print(cnt-1)

    

    
    


