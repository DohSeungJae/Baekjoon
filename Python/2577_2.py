a=int(input())
b=int(input())
c=int(input())

cnt=[0]*10
multi=str(a*b*c)

for c in multi:
    cnt[int(c)]+=1

for n in cnt:
    print(n)
    

