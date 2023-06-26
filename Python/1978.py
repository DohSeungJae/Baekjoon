import sys
input=sys.stdin.readline

n=int(input())

nums=list(map(int,input().split()))
cnt=0

def judge(a):
    for i in range(2,a):
        if(a%i==0):
            return 0
        
    return 1 


while(nums):
    a=nums.pop()
    if(a==1):
        continue
    
    if(judge(a)):
        cnt+=1
    
    
print(cnt)

