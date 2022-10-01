#oxo 가능 ooo 불가능 oxox 가능

import sys
input = sys.stdin.readline


N = int(input())

red, green, blue = [],[],[]
dp = [[0 for _ in range(3)] for _ in range(N)]

for _ in range(N):
    R,G,B = map(int,input().split()) 
    red.append(R)
    green.append(G)
    blue.append(B)


dp[0][0], dp[0][1], dp[0][2] = red[0], green[0], blue[0]

for i in range(1,N):
    dp[i][0] = red[i] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = green[i] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = blue[i] + min(dp[i-1][1], dp[i-1][0])

print(min(dp[-1]))