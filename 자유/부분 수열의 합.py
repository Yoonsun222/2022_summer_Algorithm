import sys
from collections import deque

N, S = map(int,input().split())
lst = list(map(int,input().split()))


def bfs(start):
    
    answer = 0
    sv = lst[start]
    stack = deque()
    stack.append([start,sv])
    

    while stack:
        start,sv = stack.pop()
        if sv == S:
            answer += 1
        #print(start,sv)
        if start != N-1:
            for i in range(start+1,N):
                val = sv + lst[i]
                stack.append([i,val])

    return answer

answer = 0

for i in range(N):
    answer += bfs(i)
    # print('----------')

print(answer)