from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


for _ in range(m):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)


queue = deque()
queue.append(1)
visited[1] = 1
cnt = 0

while queue:
    current = queue.popleft()
    cnt += 1

    for i in graph[current]:
        if visited[i] == 1:
            continue
        queue.append(i)
        visited[i] = 1

print(cnt-1)