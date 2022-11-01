

from collections import deque
import heapq

import sys

input = sys.stdin.readline


t = int(input())



for _ in range(t):
    n = int(input())
    rank = list(map(int,input().split()))
    v = int(input())
    
    state = True
    heap = []
    result = []
    indegree = [0] * (n+1)
    visited = [0] * (n+1)
    pre = 0
    
    #몇번쨰 순위인지 차수로 넣어줌 
    # 1등은 0이 아닌 1임
    for r in rank:
        indegree[r] += indegree[pre]+1
        pre = r

    #바뀐 순위 입력을 받은 다음, 현재 존재하는 순위와 받은 순위의 일관성 만족하면 heap에 넣어주고
    #그렇지 않으면 바로 임파서블 때려버리게 state = Fasle함
    for _ in range(v):
        i,j = map(int,input().split())
        if indegree[i] > indegree[j]:
            heapq.heappush(heap,[indegree[i],i,j])
        else:
            state = False

    #state == False시에는 바로 임파서블 프린트하고 뒤에 할 것도 없이 다음 테스트케이스 ㄱㄱ
    if state == False:
        print("IMPOSSIBLE")
        continue
    
    #만약 일관성이 있으면 while heap을 돌면서
    #heap 쓴 이유는 기존에 순위가 높은 애들부터 바꿔야 하니까~ 그렇게 했음..
    #해서 indegree에 i,j의 차수의 차이값을 더하고 뺀 다음 새로운 순위 생성
    while heap:
        r,i,j = heapq.heappop(heap)
        d = abs(indegree[i]-indegree[j])
        indegree[i] -= d
        indegree[j] += d

    
    #앞선 순위부터 프린트하기 위해 result라는 heap구조에 넣음
    #다만 순위가 중복되면 ? 를 출력해야되기 때문에 visited로 검증
    for i in range(1,n+1):
        heapq.heappush(result, [indegree[i], i])
        if indegree[i] > n or indegree[i] < 1:
            state = False
            break
        if visited[indegree[i]] != 0:
            state = False
            break
        visited[indegree[i]] = 1
    
    if state == False:
        print("?")
        continue
    
    #순위 프린트
    while result:
        ans = heapq.heappop(result)
        print(ans[1], end = " ")
    print()
    
