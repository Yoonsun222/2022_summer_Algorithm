from collections import deque

n, m = map(int,input().split())

def dfs():
    queue = deque()
    queue.append([n,0])
    visited=[0 for _ in range(200001)] 

    while queue:
        subin, cnt = queue.popleft()
        if subin == m:
            return cnt
        
        twice, plus, minus = 2 * subin, subin + 1, subin - 1
        if 0 <= twice <= 200000 and visited[twice] == 0:
            queue.append([twice,cnt+1])
            visited[twice] = 1
        if 0 <= minus <= 200000 and visited[minus] == 0:
            queue.append([minus,cnt+1])
            visited[minus] = 1
        if 0 <= plus <= 200000 and visited[plus] == 0:
            queue.append([plus,cnt+1])
            visited[plus] = 1

print(dfs())