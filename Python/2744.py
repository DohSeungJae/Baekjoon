import sys
input=sys.stdin.readline

string=input().strip()
for s in string:
    if s.islower():
        print(s.upper(),end="")
    else:
        print(s.lower(),end="")
        