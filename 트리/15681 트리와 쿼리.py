import sys

input = sys.stdin.readline


n, r, q = map(int,input().split())
tree = [[] for _ in range(n+1)]


# 트리는 dfs
# leaf노드 부터 올라오면서 더해야 한다

for _ in range(n-1):
    n1, n2 = map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

dp = [0 for _ in range(n+1)]

def dfs(node):
    dp[node] = 1

        
    for i in tree[node]:
        if dp[i] == 0:
            dfs(i)
            dp[node] += dp[i]
    return

    
dfs(r)

for _ in range(q):
    n = int(input())
    print(dp[n])