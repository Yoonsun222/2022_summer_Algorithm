from collections import deque
import sys


input = sys.stdin.readline

n, m = map(int,input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    pd = list(map(int,input().split()))
    k = pd[0]
    for i in range(1,k):
        graph[pd[i]].append(pd[i+1])

    for i in range(2,k+1):
        indegree[pd[i]] += 1
    

queue = deque()
result = []

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    result.append(current)

    for i in graph[current]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)