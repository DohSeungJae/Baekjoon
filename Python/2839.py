import sys
input=sys.stdin.readline

n=int(input())

sugar=[-1,-1,-1,1,-1,1,2,-1]


for _ in range(n-7):
    temp=[]
    for i in range(len(sugar)-1,2,-1):
        
        if(sugar[i]!=-1 and sugar[-i]!=-1):
            temp.append(sugar[i]+sugar[-i])

    sugar.append(min(temp))

print(sugar[n])









    



                



