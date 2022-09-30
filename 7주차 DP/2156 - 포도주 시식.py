import sys

input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(n)]
lst = [int(input()) for _ in range(n)]
dp[0] = lst[0]


for i in range(n):
    if i == 0:
        dp[0] = lst[0]
        continue
    elif i == 1:
        dp[1] = lst[0]+lst[1]        
        continue
    elif i == 2:
        dp[2] = max(lst[0],lst[1])+lst[2]
        continue
    elif i == 3:
        dp[3]= lst[i] + max(dp[i-2],dp[i-3]+lst[i-1])
        continue
    dp[i]= lst[i] + max(dp[i-2],dp[i-3]+lst[i-1],dp[i-4]+lst[i-1])


print(max(dp))
    