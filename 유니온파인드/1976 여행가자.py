import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())


parent = [i for i in range(N+1)]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] == 1:
            union_parent(parent,i+1,j+1)

state = True

tmp = list(map(int,input().split()))
ans = find_parent(parent, tmp[0])

for i in range(M):
    if find_parent(parent, tmp[i]) != ans:
        state = False

if state:
    print("YES")
else:
    print("NO")
