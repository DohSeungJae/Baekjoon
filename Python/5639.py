import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if key<root.value:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)

    return root

def post(root):
    if root:
        post(root.left)
        post(root.right)
        print(root.value)

root=Node(int(input()))
while True:
    try:
        node=int(input())
        insert(root,node)
    except:
        break

post(root)

#5639 이진 검색 트리 only pypy3