list_string=[]
while 1:
    string=input()
    if string!="***":
        list_string.append(string)
    else:
        break

for string in list_string:
    for i in string[::-1]:
        print(i,end="")
    print()
    