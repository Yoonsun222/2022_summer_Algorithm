from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
time = {}
indegree = [0 for _ in range(N+1)]


for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    time[i] = tmp[0]
    for j in tmp[1:-1]:
        indegree[i] += 1
        graph[j].append(i)


queue = deque()

for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

answer = [0 for _ in range(N+1)] 

while queue:
    current = queue.popleft()
    answer[current] += time[current]    

    
    for i in graph[current]:
        indegree[i] -= 1
        answer[i] = max(answer[i],answer[current])
        if indegree[i] == 0:
            queue.append(i)

for i in range(1,N+1):
    print(answer[i])