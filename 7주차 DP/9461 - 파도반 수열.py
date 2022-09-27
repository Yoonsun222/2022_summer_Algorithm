
T = int(input())
dp = [ 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(90)]
for i in range(11,101):
    dp[i] = dp[i-3]+dp[i-2]

for _ in range(T):
    N = int(input())
    print(dp[N])
