#퀸은 상하좌우 대각선 다 이동 가능
#행과 열 겹치면 안된다. 한 행에 하나만 가능
#이전 행의 대각선에 위치하면 안된다.

N = int(input())

answer = 0

row = [0 for _ in range(N)]


def backtracking(row, start):
    global answer

    
    if start == N:
        answer += 1
        return
   
    
    for j in range(N):
        state = True
        row[start] = j
        for i in range(start):
            if row[i]==row[start] or abs(row[i] - j) == abs(i-start):
                state = False
                break
        if state == True:
            backtracking(row, start+1)



backtracking(row, 0)
print(answer)