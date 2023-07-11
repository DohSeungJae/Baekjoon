import sys
input=sys.stdin.readline

o_list=[]
for _ in range(7):
    n=int(input())
    if(n%2==1):
        o_list.append(n)
if(len(o_list)==0):
    print(-1)
else:
    print(sum(o_list))
    print(min(o_list))
    

