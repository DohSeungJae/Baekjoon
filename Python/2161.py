import queue
import sys
input=sys.stdin.readline

n=int(input())
q=queue.Queue()
res=[]

for i in range(n):
    q.put(i+1)

while(q.qsize()!=1):
    res.append(q.get())
    q.put(q.get())

res.append(q.get())
print(*res)
    