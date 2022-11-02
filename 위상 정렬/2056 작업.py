from collections import deque
import sys

input = sys.stdin.readline

n = int(input())


graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)

for i in range(1,n+1):
    work = list(map(int,input().split()))
    time[i] = work[0]
    if work[1]:
        pre_work = work[2:]
        for j in range(work[1]):
            graph[pre_work[j]].append(i)
            indegree[pre_work[j]] += 1
    
queue = deque()
result = [0 for _ in range(n+1)]

for i in range(n+1):
    if indegree[i] == 0:
        queue.append(i)

print(indegree)
print(queue)

while queue:
    current = queue.popleft()
    result[current] += time[current]

    for i in graph[current]:
        indegree[i] -= 1
        result[i] = max(result[i],result[current])
        if indegree[i] == 0:
            queue.append(i)

print(result)
print(max(result))