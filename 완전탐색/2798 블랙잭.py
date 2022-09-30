#방법 1

N, M = map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
answer = 0
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      pre_answer = lst[i]+lst[j]+lst[k]
      if answer < pre_answer and pre_answer <= M:
        answer = pre_answer

print(answer)


#방법2 

import itertools

n, m = map(int,input().split())
numbers = list(map(int,input().split()))
comb = itertools.combinations(numbers,3)
answer = 0
for numb in comb:
    c_ans =sum(numb)
    if  c_ans <= m:
        answer = max(answer,c_ans)

print(answer)