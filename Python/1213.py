import sys
input=sys.stdin.readline

name=str(input().strip())

name_list=[]

for i in name:
    name_list.append(i)

name_list.sort(reverse=True)

list_temp=[]
for i in name_list:
    if i in list_temp:
        list_temp.pop(list_temp.index(i))
    else:
        list_temp.append(i)


if(len(list_temp)>1):
    print("I'm Sorry Hansoo")

else:
    m=''
    for i in range(len(list_temp)):
        m=name_list.pop(name_list.index(list_temp[0]))

    res=''
    while(name_list):
        name_list.pop()
        res=res+name_list.pop()

    res=res+m+res[::-1]

    print(res)
    

    

    
    
    



