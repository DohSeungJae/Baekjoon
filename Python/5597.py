import sys
input=sys.stdin.readline

s_list=[i for i in range(1,31)]

for _ in range(28):
    s_list.remove(int(input()))

for s in s_list:
    print(s)
    