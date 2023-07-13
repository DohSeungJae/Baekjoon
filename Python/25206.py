import sys
input=sys.stdin.readline

avg=0.0
n_sum=0
for _ in range(20):
    str_list=list(map(str,input().strip().split()))
    g=str_list[2]
    n=int(float(str_list[1]))
    if(g!='P'):

        if(g=="A+"):
            g=4.5
        elif(g=="A0"):
            g=4.0
        elif(g=="B+"):
            g=3.5
        elif(g=="B0"):
            g=3.0
        elif(g=="C+"):
            g=2.5
        elif(g=="C0"):
            g=2.0
        elif(g=="D+"):
            g=1.5
        elif(g=="D0"):
            g=1.0
        elif(g=="F"):
            g=0

            
        avg+=g*n
        n_sum+=n

print(avg/n_sum)



        

