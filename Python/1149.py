import sys
input=sys.stdin.readline

n=int(input())
cost_rgb=[[0,0,0]]
for i in range(1,n+1):
    cost_rgb.append(list(map(int,input().split())))
    
    cost_rgb[i][0]+=min(cost_rgb[i-1][1],cost_rgb[i-1][2])
    cost_rgb[i][1]+=min(cost_rgb[i-1][0],cost_rgb[i-1][2])
    cost_rgb[i][2]+=min(cost_rgb[i-1][1],cost_rgb[i-1][0])

print(min(cost_rgb[n]))
