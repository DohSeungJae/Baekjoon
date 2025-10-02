n=int(input())
array=list(map(int,input().split()))

array.sort(reverse=True)

target=0
while True:
    target+=1

    tmp=target
    for i in range(n):
        if(tmp<array[i]): #현재 남아있는 수보다 큰 수는 고려하지 않음
            continue
        tmp-=array[i]
        if(tmp==0): #뺐을 때 0원이면 만들 수 있는 금액.
            break

    if(tmp!=0): #뺐을 때 음수이면 만들 수 없는 금액.
        print(target)
        break
