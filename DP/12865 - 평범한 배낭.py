import sys
input = sys.stdin.readline

N, K = map(int,input().split())

#mybag = [[3, 6], [4, 8], [5, 12], [6, 13]]

mybag = []

for i in range(N):
    W, V = map(int,input().split())
    mybag.append([W,V])

mybag.sort()

dp = []

for i in range(N):
    for j in range(K):

answer = []

def backtracking(start,weight, value):
    if start == N:
        answer.append(value)
        return

    for i in range(start,N):
        total_w = weight + mybag[i][0]
        if total_w <= K:
            total_v = value + mybag[i][1]
            backtracking(i+1,total_w, total_v)
        else:
            answer.append(value)
            return


backtracking(0,0,0)
#print(answer)
print(max(answer))
