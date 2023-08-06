import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    mbti=list(map(str,input().strip().split()))
    dist_min=sys.maxsize

    if(n>32):
        print(0)
        continue

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                dist=0
                for idx in range(4):
                    if(mbti[i][idx]!=mbti[j][idx]): dist+=1
                    if(mbti[j][idx]!=mbti[k][idx]): dist+=1
                    if(mbti[i][idx]!=mbti[k][idx]): dist+=1

                if(dist<dist_min):
                    dist_min=dist

                
    print(dist_min)




