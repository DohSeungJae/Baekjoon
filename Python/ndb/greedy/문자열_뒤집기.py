s=input()

group=1

a=s[0]
for i in range(1,len(s)):
    if(a!=s[i]):
        group+=1
        a=s[i]

print(group//2)

