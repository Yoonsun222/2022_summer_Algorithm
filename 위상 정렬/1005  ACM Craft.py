from collections import deque
import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())

    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    time = [0]+list(map(int,input().split()))

    for _ in range(m):
        i,j = map(int,input().split())
        graph[i].append(j)
        indegree[j] += 1

    w = int(input())

    queue = deque()
    result = [0 for _ in range(n+1)]

    for i in range(n+1):
        if indegree[i] == 0:
            queue.append(i)
            


    while queue:
        current = queue.popleft()
        result[current] += time[current]

        for i in graph[current]:
            indegree[i] -= 1
            result[i] = max(result[i],result[current])
            if indegree[i] == 0:
                queue.append(i)

    print(result[w])