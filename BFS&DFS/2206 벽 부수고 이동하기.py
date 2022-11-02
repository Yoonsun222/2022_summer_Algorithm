# 벽을ㅇ 부숴야 하는데.. 벽 부수는건 단 1번ㅁ난 가능
#  1,0으로 표시 
# 0은 이동 가능 1은 이동 불가
# 벽 뚫었는데 이후엔 접근 못하는 경우..? 이 경우.. visited[yy][xx] 가 최소로 잡히기 때문에 다른 방안이 필요함
# 3차원 배열 ;; 0이면 벽 안 뚫고 가는 경우 1이면 벽 뚫고 가는 경우


from collections import deque   

n, m = map(int,input().split())
graph = []
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
for _ in range(n):
    lst = list(map(int,input()))
    graph.append(lst)


dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque()
queue.append([0,0,0])
visited[0][0][0] = 1
answer = 0

while queue:
    y,x,w = queue.popleft()

    if y == n-1 and x == m-1:
        answer = visited[y][x][w]
        break
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if xx < 0 or xx >= m or yy >= n or yy < 0:
            continue
        if graph[yy][xx] == 0 and visited[yy][xx][w] == 0:
            visited[yy][xx][w] = visited[y][x][w]+1
            queue.append([yy,xx,w])
        elif graph[yy][xx] == 1 and w == 0:
            visited[yy][xx][1] = visited[y][x][w] + 1
            queue.append([yy,xx,1])

if answer:
    print(answer)
else:
    print(-1)