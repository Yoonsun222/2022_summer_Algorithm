from collections import deque
import sys


N = int(input())


graph = [list(map(int,input())) for _ in range(N)]
#graph = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

def dfs(start,visited):
    stack = deque()
    stack.append([start[0], start[1]])
    cnt = 0
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    while stack:
        x,y = stack.pop()
        if visited[y][x] == 0:
            cnt += 1
        visited[y][x] = 1
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < N and 0 <= yy < N and visited[yy][xx] == 0 and graph[yy][xx]==1:
                stack.append([xx,yy])
    return cnt

cnt = 0
answer = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            tmp_ans = dfs([j,i], visited)
            answer.append(tmp_ans)
            cnt += 1

answer.sort()

print(cnt)
for ans in answer:
    print(ans)