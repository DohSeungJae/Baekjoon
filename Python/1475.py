import math
n=str(input())
cnt=[0]*9 #9는 6과 같이 계산하기 때문에 제외

for c in n:
    if(c=="9"):c="6"
    cnt[int(c)]+=1

#cnt[6]=math.ceil(cnt[6]/2) #9까지 같이 계산 //내가 작성한 코드
cnt[6]=(cnt[6]+1)//2 #더 나은 코드
print(max(cnt))