#퀸은 상하좌우 대각선 다 이동 가능


N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

def backtracking(graph,cnt, startx,starty):
    global answer
    if cnt == N:
        answer += 1
        return

    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [1,-1,0,0,-1,1,1,-1]
    for yy in range(starty,N):
        if xx == N-1:
            startx = 0
              
        for xx in range(startx,N):
            state = True

            if graph[yy][xx] == 1:
                continue
            for i in range(8):
                x = dx[i] + xx
                y = dy[i] + yy
                if x < 0 or N <= x or y < 0 or N <= y: 
                    continue
                if graph[y][x] == 1:
                    state = False
                    break
                      
            if state == True:
                graph[yy][xx] = 1
                backtracking(graph,cnt+1,xx,yy)
                graph[yy][xx] = 0
            
backtracking(graph,0,0,0)    

print(answer)
        
