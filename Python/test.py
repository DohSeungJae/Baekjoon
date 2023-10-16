numList=[4,8,12]
size=50

for i in numList:
    for j in range(i*2,size,i):
        print(j)


for i in numList:
    for j in range(2,size):
        mul=i*j
        if mul>size:
            continue
        
        print(mul)

        