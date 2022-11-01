

n = int(input())
lst = list(map(int,input().split()))
dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
max_val = 0

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp1[i] = max(dp1[j] + 1, dp1[i])
        if lst[n-i-1] > lst[n-j-1]:
            dp2[n-i-1] = max(dp2[n-i-1], dp2[n-j-1]+1)
for i in range(n):
    if max_val < dp1[i]+dp2[i]:
        max_val = dp1[i]+dp2[i]

print(max_val-1)
