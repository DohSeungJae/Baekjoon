s=input()

summary=0
result=[]

for c in s:
    if (65<=ord(c)<=90):
        result.append(c)
    else:
        summary+=int(c)

result.sort()
for c in result:
    print(c,end="")
print(summary)
