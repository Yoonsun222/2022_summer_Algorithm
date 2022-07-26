
def cal(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    return cal(n-2) + cal(n-1)

n = int(input())
print(cal(n))