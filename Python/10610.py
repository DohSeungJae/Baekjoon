import sys
input=sys.stdin.readline

num_str=input().strip()
if '0' not in num_str:
    print(-1)

else:
    num_list=[]

    for str_ in num_str:
        num_list.append((str_))
    num_list.sort(reverse=True)


    res=''
    for num in num_list:
        res+=num
    
    if(int(res)%30==0):
        print(res)
    else:
        print(-1)
        

