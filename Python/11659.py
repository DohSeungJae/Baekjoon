import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n_list=list(map(int,input().split()))

sum_list=[]
sum_list.append(0)
for n in n_list:
    sum_list.append(sum_list[-1]+n)

for _ in range(m):
    i,j=map(int,input().split())
    print(sum_list[j]-sum_list[i-1])




