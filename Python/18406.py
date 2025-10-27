n=input()

length=len(n)
result=0
for i in range(length//2):
    result=result+int(n[i])-int(n[(length//2)+i])

if(result==0):
    print("LUCKY")
else:
    print("READY")   