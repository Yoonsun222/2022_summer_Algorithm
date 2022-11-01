from collections import deque
import sys
import heapq

input = sys.stdin.readline
n, m = map(int,input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    i,j = map(int,input().split())
    graph[i].append(j)
    indegree[j] += 1


heap = []
result = []

for i in range(n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)


while heap:
    current = heapq.heappop(heap)
    result.append(current)

    for i in graph[current]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap,i)

result = result[1:]
print(*result)