

from collections import deque
import heapq

t = int(input())



for _ in range(t):
    n = int(input())
    rank = list(map(int,input().split()))
    v = int(input())
    
    state = True
    heap = []
    result = []
    indegree = [0] * (n+1)
    visited = [0] * (n+1)
    pre = 0
    
    for r in rank:
        indegree[r] += indegree[pre]+1
        pre = r

    for _ in range(v):
        i,j = map(int,input().split())
        if indegree[i] < indegree[j]:
            heapq.heappush(heap,[indegree[i],i,j])
        else:
            state = False
            break
    if state == False:
        print("IMPOSSIBLE")
        continue
    
    while heap:
        r,i,j = heapq.heappop(heap)
        d = indegree[i]-indegree[i]
        indegree[i] += d
        indegree[j] -= d

    queue = deque()

    for i in range(1,n+1):
        heapq.heappush(result, [indegree[i], i])
        if visited[indegree[i]] != 0:
            state = False
            break
        visited[indegree[i]] = 1
    
    if state == False:
        print("?")
    
    while result:
        print



result = result[1:]
print(*result)