import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
nums=list(map(int,input().split()))

nums.sort()
first=nums.pop()
second=nums.pop()
group_size=(first*K)+second

group_cnt=M//(K+1)
rest=M%(K+1)

result=(group_cnt*group_size)+(rest*first)

print(result)


