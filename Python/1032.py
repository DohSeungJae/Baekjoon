import sys
input=sys.stdin.readline

N=int(input())
cmd=input().strip()
res=[cmd[i] for i in range(len(cmd))]

for _ in range(N-1):
    cmd=input().strip()
    for i in range(len(cmd)):
        if(res[i]!=cmd[i] and res[i]!="?"):
            res[i]="?"

for i in res:
    print(i,end="")
