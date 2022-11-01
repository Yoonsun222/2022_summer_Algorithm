
T = int(input())

for _ in range(T):
    k = int(input())
    lst = list(map(int,input().split()))
    dp = [[[0 for _ in range(k)] for _ in range(k)]]
    sum_lst = [0 for _ in range(k+1)]
    for i in range(1,k):
        sum_lst[i] = sum_lst[i-1] + lst[i]
    sum_lst = [0] + sum_lst
    
    for i in range(1,k):
        for j in range(k-i):
            l = i+j
            dp[j][l] = 1e9
            for o in range(j,l):
                dp[j][l] = min(dp[j][l],dp[j][o]+dp[o+1][l]+sum_lst[l+1]-sum_lst[j])
    
    print(dp[0][k-1])
