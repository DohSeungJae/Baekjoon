import sys
input=sys.stdin.readline

init_pos=str(input())
y=int(init_pos[1])
x=ord(init_pos[0])-ord('a')+1

cases_yx=[[2,1],[2,-1],[-2,1],[-2,-1], [1,2],[1,-2],[-1,2],[-1,-2]]

case_cnt=0
for next_yx in cases_yx:
    next_y=next_yx[0]+y
    next_x=next_yx[1]+x

    if(next_y>8 or next_y<1):
        continue
    if(next_x>8 or next_x<1):
        continue

    case_cnt+=1

print(case_cnt)