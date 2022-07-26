def cal(n):
    if n == 1 or n== 0:
        return 1
    return n * cal(n-1)
n = int(input())
print(cal(n))