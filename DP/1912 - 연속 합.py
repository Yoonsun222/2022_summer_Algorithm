
N = int(input())
lst = list(map(int,input().split()))

dp = [0 for _ in range(N)]

dp[0] = lst[0]

max_val = dp[0]

for i in range(1,N):
    if dp[i-1] > 0:
        dp[i] = dp[i-1]+lst[i]
    else:
        dp[i] = lst[i]

    if max_val < dp[i]:
        max_val = dp[i]
print(dp)
print(max_val)