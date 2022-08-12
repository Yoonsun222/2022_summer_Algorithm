from collections import deque
import sys


input = sys.stdin.readline



N,M = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N)]
#graph = [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]


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
            if 0 <= xx < M and 0 <= yy < N and visited[yy][xx] == 0 and graph[yy][xx]==1:
                stack.append([xx,yy])
    return cnt

max_ans = 0
answer = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            tmp_ans = dfs([j,i], visited)
            if tmp_ans > max_ans:
                max_ans = tmp_ans
            answer += 1

print(answer)
print(max_ans)