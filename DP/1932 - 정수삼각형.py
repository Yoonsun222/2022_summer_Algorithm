import sys

input = sys.stdin.readline


n = int(input())
answer = [[int(input())]]

for i in range(2,n+1):
    lst = list(map(int,input().split()))
    for j in range(i):
        if j == i-1:
           lst[j] += answer[0][-1]
        elif j == 0:
            lst[j] += answer[0][0]
        else:
            lst[j] += max(answer[0][j],answer[0][j-1]) 
    answer.pop()
    answer.append(lst)

print(max(answer[0]))