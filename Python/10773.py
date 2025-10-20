import sys
input=sys.stdin.readline

n=int(input())
st=[] #stack
for _ in range(n):
    inte=int(input()) #integer
    if(inte):st.append(inte)
    else: st.pop()

print(sum(st))
