import sys
input=sys.stdin.readline

n=int(input())
d={}

for _ in range(n):
    book=str(input()).strip()
    
    if(book in d.keys()):
        d[book]+=1
    else:
        d[book]=1

maxi=max(d.values())

book_list=list(d.keys())
book_list.sort()

for b in book_list:
    if(d[b]==maxi):
        print(b)
        break
    

