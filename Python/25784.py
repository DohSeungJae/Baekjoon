import sys
input=sys.stdin.readline

n_list=list(map(int,input().split()))

n_list.sort()
maxi=n_list.pop()

if(n_list[0]+n_list[1]==maxi):
    print(1)
elif(n_list[0]*n_list[1]==maxi):
    print(2)
else:
    print(3)
    
