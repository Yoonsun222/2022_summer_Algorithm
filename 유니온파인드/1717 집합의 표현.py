import sys

sys.setrecursionlimit(10**6)

def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    check, a, b = map(int,input().split())
    if check == 0:
        union_parent(parent,a,b)
    elif check == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")