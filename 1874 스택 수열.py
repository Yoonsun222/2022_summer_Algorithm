import sys 
input = sys.stdin.readline


N = int(input())

lst = [int(input()) for i in range(N)]

ans_pm, tmp = [], []
cnum, idx = 1, 0

while idx < N:  #idx로 lst의 0부터 N-1까지 검토
    if tmp and tmp[-1] == lst[idx]: #만약 tmp에 값이 존재 하고 tmp의 맨 마지막 값이 해당 인덱스의 lst값과 같으면
        idx += 1    #idx를 +1을 하여 이후에 lst[idx+1]값을 찾게 만들고
        tmp.pop()   #tmp[-1] 값을 pop한다.
        ans_pm.append('-') #그리고 정답에 -를 집어 넣음
    elif cnum > N: # 만약 cnum이 idx보다 커지면 'NO'출력
        print('NO')
        break
    else:
        tmp.append(cnum) #위의 모든 경우에 해당이 안되면 cnum을 tmp에 append
        ans_pm.append('+') # 정답에 + 넣음
        cnum += 1 # cnum +1

if idx == N:
    for i in ans_pm:
        print(i)




###회고
# cnum을 리스트로 만들어서 cnum을 리스트로 만든것과 lst를 비교하려고 했다.
# 첫 시도는 실패였고, 원래의 아이디어에서 새로운 아이디어로 생각을 바꾸기 어려웠음
# 12시간 뒤에 이전것을 잊고 다시 풀었는데... 만약 실제 코테 때 이런 경우가 발생하면
# 어떻게 해야하는지....ㅠ
