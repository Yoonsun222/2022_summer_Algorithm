
n = int(input())

dp = [0 for _ in range(n)]
A = [0 for _ in range(n)]
B = [0 for _ in range(n)]

for i in range(n):
    a,b = map(int, input().split())
    A[i], B[i] = a, b

for i in range(n):
    for j in range(i):
        if B[i] > B[j] :
