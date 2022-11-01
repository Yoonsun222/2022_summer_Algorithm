
# 왜 dp문제인가?
# 2차원 dp로 s과 e를 나타내자
# 만약 s와 e가 팰린드롬이면 s+1과 e-1도 팰린드롬이다.

n = int(input())
lst = [0] + list(map(int,input().split()))
t = int(input())

dp = [[ 0 for _ in range(n+1)] for _ in range(n+1)]

def is_palindrome(s,e):
    mid = (s+e)//2
    state = True
    if (e-s)%2:
        r = min(mid,n-mid+1)
        for i in range(r):
            if state == False:
                dp[mid-i][mid+1+i] = -1
            elif lst[mid-i] == lst[mid+1+i]:
                dp[mid-i][mid+1+i] = 1
            else:
                dp[mid-i][mid+1+i] = -1
                state = False
    else:
        r = min(mid, n-mid+1)
        for i in range(r):
            if state == False:
                dp[mid-i][mid+i] = -1
            elif lst[mid-i] == lst[mid+i]:
                dp[mid-i][mid+i] = 1
            else:
                dp[mid-i][mid+i] = -1
                state = False

    return

for _ in range(t):
    s,e = map(int,input().split())
    
    if dp[s][e] == 0:
        is_palindrome(s,e)
    if dp[s][e] == -1:
        print(0)
    else:
        print(1)
    