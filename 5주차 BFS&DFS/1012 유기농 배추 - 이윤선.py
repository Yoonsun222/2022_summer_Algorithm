from collections import deque
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1



    def bfs(start):
        q = deque()
        q.append(start)
        dx, dy = [0,0,1,-1], [1,-1,0,0]
        
        while q:
            x,y = q.popleft()
            if visited[y][x] == 1:
                continue
            visited[y][x] = 1
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if xx < 0 or yy < 0 or xx >= M or yy >= N:
                    continue
                if graph[yy][xx] == 1 and visited[yy][xx] == 0:
                    q.append([xx,yy])
        return 0

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs([j,i])
                count += 1
    
    print(count)
