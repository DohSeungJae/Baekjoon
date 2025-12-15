n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input().strip().split())))

lst.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for one in lst:
    print(one[0])