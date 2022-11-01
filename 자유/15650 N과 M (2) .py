# 중복없이 N개를 고른 수열 즉 조합을 찾아라 이 말인가~~?


N, M = map(int,input().split())
lst = [0 for _ in range(M)]

def backtracking(lst,idx,start):

    if lst[-1] != 0:
        print(" ".join(map(str,lst)))
        return 
    for i in range(start,N+1):
        lst[idx] = i
        backtracking(lst,idx+1,i+1)
        lst[idx] = 0
        
backtracking(lst,0,1)
        




