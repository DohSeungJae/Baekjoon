import sys
input=sys.stdin.readline

class Node:
    def __init__(self,key):
        self.key=key
        self.children={}

class Trie:
    def __init__(self):
        self.head=Node(None)
    def insert(self,string):
        curNode=self.head
        for c in string:
            if c not in curNode.children:
                curNode.children[c]=Node(c)
            curNode=curNode.children[c]

def printNodes(curNode:Node, i:int, isHead=0):
    if(not isHead):
        print("--"*i+curNode.key)
    sortedKeys=sorted(curNode.children.keys())
    for child in sortedKeys:
        printNodes(curNode.children[child],i+1)

N=int(input())
trie=Trie()
for _ in range(N):
    path=list(map(str,input().split()))[1:]
    trie.insert(path)

printNodes(trie.head,-1,1)