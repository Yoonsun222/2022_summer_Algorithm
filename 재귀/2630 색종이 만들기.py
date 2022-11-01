
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())

# board = [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
board = [list(map(int,input().split())) for _ in range(n)]
black, white = 0, 0

def div(n,st_x,st_y,ed_x,ed_y):
    global black, white
    tmp = 0 
    if n == 1:
        if board[st_y:ed_y][st_x:ed_x]:
            black += 1
        else:
            white += 1
        return

    for i in range(st_y,ed_y):
        for j in range(st_x,ed_x):
            tmp += board[i][j]   
    if tmp == 0:
        # print(1,st_x,st_y,ed_x,ed_y)
        white += 1
        return
    if tmp == n*n:
        # print(2,st_x,st_y,ed_x,ed_y)
        black += 1
        return
    
    
    #1사분면
    div(n//2, st_x, st_y, ed_x//2, ed_y//2)
    #2사분면
    div(n//2, ed_x//2, st_y, ed_x, ed_y//2)
    #3사분면
    div(n//2, st_x, ed_y//2, ed_x//2, ed_y)
    #4사분면
    div(n//2, ed_x//2, ed_y//2, ed_x, ed_y)
    return


div(n,0,0,n,n)

print(white)
print(black)