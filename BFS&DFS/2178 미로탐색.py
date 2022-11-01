

from collections import deque

n,m = map(int,input().split())

board = [list(map(int,input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
#board = [[1,0,1,1,1,1], [1,0,1,0,1,0], [1,0,1,0,1,1], [1,1,1,0,1,1]]
#print(board)

def dfs(x,y,visited):  

    queue = deque([[x,y]])
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    visited[y][x] = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if xx < 0 or yy < 0 or xx >= m or yy >= n:
                continue
            if board[yy][xx] == 0:
                continue

            if visited[yy][xx] == 0:
                queue.append([xx,yy])
                visited[yy][xx] = visited[y][x]+1
            elif visited[yy][xx] > visited[y][x]+1:
                visited[yy][xx] = visited[y][x]+1
                queue.append([xx,yy])
    return visited[-1][-1]

print(dfs(0,0,visited))
