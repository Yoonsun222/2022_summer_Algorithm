
N = int(input())

dp = [1,2] + [0 for _ in range(N-2)]
for i in range(2,N):
    dp[i] = (dp[i-1] +dp[i-2]) % 15746

print(dp[-1])