#2309
import sys
input=sys.stdin.readline
h_list=[]

for _ in range(9):
    h_list.append(int(input()))

h_list.sort()

a=sum(h_list)-100

for i in range(9):
    for j in range(9):
        if(h_list[i]+h_list[j]==a and h_list[i]!=h_list[j]):
            e1=h_list[i] 
            e2=h_list[j]
            break
            

for h in h_list:
    if(h!=e1 and h!=e2):
        print(h)


        

    
