import sys
input = sys.stdin.readline

N, M = map(int,input().split())
INF = 1e9

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1



for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
answer = 0
min_sum = 1e9 * N+1
#print(graph)
for l in range(1,N+1):
    csum = sum(graph[l])%1e9
    if min_sum > csum:
        answer = l
        min_sum = csum
        #print(min_sum, answer)

print(answer)