full_length,length=map(int,input().split())
li=list(map(int,input().split()))

start=sum(li[:length])
max_val=start
count=1
for i in range(length,full_length):
    start=start-li[i-length]+li[i]
    if(max_val<start):
        max_val=start
        count=1
    elif (max_val==start):
        count+=1
    else:
        continue

if max_val==0:
    print("SAD")
else:
    print(max_val)
    print(count)
    