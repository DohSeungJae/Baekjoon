n=int(input())

score=[]
for _ in range(n):
    score.append(list(map(str,input().split())))
    #이름,국,영,수

score.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for line in score:
    print(line[0])

