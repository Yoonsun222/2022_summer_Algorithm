#움직일때마다 생명 1씩 소모되는 구역과 안그런구역이 있음
from collections import deque
import sys


input = sys.stdin.readline


def danger(graph,num,N):
    for _ in range(N):
        X1, Y1, X2, Y2 = map(int,input().split())
        for i in range(min(Y1,Y2), max(Y1,Y2)+1):
            for j in range(min(X1,X2), max(X1,X2)+1):
                graph[i][j] = num



def bfs(graph):

    q = deque()
    q.append([0,0,0])
    visited = [[0 for _ in range(501)] for _ in range(501)]
    dx,dy = [0,0,1,-1], [1,-1,0,0]
    answer = []
    while q:
        y, x, life = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0>= xx and xx <= 500 and 0>= yy and yy <= 500:
                continue
            if graph[yy][xx] == 2:
                continue
            
            lose_life = graph[yy][xx]
            cur_life = visited[x][y] + lose_life
                
            if visited[yy][xx] == 0:
                visited[yy][xx] = cur_life
                q.append([yy,xx])
                if xx==500 and yy == 500:
                    visited[yy][xx] = 0
                    answer.append(cur_life)
            elif visited[yy][xx] != 0:
                    visited[yy][xx] = min(visited[yy][xx], cur_life)
    return answer

graph = [[0 for _ in range(501)] for _ in range(501)]


#위험한구역 수
N = int(input())
danger(graph,1,N)

#죽음의 구역
M = int(input())
danger(graph,2,M)

graph[0][0] = 0

answer = bfs(graph)

if answer:
    print(min(answer))
else:
    print(-1)