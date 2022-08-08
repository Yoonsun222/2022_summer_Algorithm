import sys
from collections import deque
import heapq

input = sys.stdin.readline

def dfs(start, graph,N):
    stack = [start]
    cnt = 1
    visited = [0 for _ in range(N+1)]
    visit = [0 for _ in range(N+1)]
    while stack:
        node = stack.pop()
        if visited[node] == 0 :    
            visit[node] = cnt
            cnt +=1
        visited[node] = 1
        for node_node in graph[node]:
            if visited[node_node] == 0:
                stack.append(node_node)
                
    return visit



N, M, R = map(int,input().split())

graph = [[] for _ in range(N+1)]
    

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(N+1):
    graph[j].sort(reverse=True)


visit = dfs(R,graph,N)
for i in range(1,N+1):
    print(visit[i])
