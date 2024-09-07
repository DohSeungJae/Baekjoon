import sys
input=sys.stdin.readline

string=input().strip()
cur=""
fragment0=0
fragment1=0

for s in string:
    if(s!=cur):
        if(s=="0"):
            fragment0+=1
        else:
            fragment1+=1
        cur=s

print(min(fragment0,fragment1))