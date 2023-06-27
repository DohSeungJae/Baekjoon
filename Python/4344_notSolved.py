##미해결

import sys
input=sys.stdin.readline

c=int(input())

for _ in range(c):
    input_list=list(map(int,input().split()))
    m=int(input_list[0])
    m_list=[int(num) for num in input_list[1:]]
    
    avg=int(sum(m_list)/len(m_list))
    cnt=0
    for s in m_list:
        if s>avg:
            cnt+=1
    
    per=cnt/len(m_list)*100
    print("{:.3f}".format(per), end="")
    print("%")


    

