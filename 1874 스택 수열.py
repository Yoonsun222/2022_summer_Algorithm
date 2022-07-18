N = int(input())

lst = [int(input()) for i in range(N)]

ans_pm, tmp = [], []
cnum, idx = 1, 0

while idx < N:
    if tmp and tmp[-1] == lst[idx]:
        idx += 1
        tmp.pop()
        ans_pm.append('-')
    elif cnum > N:
        print('NO')
        break
    else:
        tmp.append(cnum)
        ans_pm.append('+')
        cnum += 1

if idx == N:
    for i in ans_pm:
        print(i)