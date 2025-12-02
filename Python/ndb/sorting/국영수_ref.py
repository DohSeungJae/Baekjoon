n=int(input())

lst=[]
for _ in range(n):
    line=list(map(str,input().split()))
    line[1],line[2],line[3]=int(line[1]),int(line[2]),int(line[3])
    lst.append(line)

lst.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for line in lst:
    print(line[0])
