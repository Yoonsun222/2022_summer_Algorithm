from collections import deque
import sys


N = int(input())


graph = [list(map(int,input())) for _ in range(N)]
#graph = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

def bfs(start,visited):
    q = deque()
    q.append([start[0], start[1]])
    visited[start[1]][start[0]] = 1
    count = 1
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 > xx  or xx >= N or yy >= N or yy < 0:
                continue  
            if visited[yy][xx] == 0 and graph[yy][xx]==1:
                q.append([xx,yy])
                visited[yy][xx] = 1
                count += 1
                
    return count

cnt = 0
answer = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            tmp_ans = bfs([j,i], visited)
            answer.append(tmp_ans)
            cnt += 1

answer.sort()
print(cnt)
for ans in answer:
    print(ans)