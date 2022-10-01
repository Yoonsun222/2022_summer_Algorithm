import sys 
input = sys.stdin.readline

def binary_search(lst,M):
    
    start = 0
    end = max(lst)

    while start <= end:
        mid = (start+end)//2
        answer = 0
        for tree in lst:
            if (tree - mid) >= 0:
                answer += (tree - mid)
        #print(answer,M)
        if answer == M:
            return mid
        elif answer < M:
            end = mid - 1
        else:
            start = mid + 1
    return end
            




N, M = map(int,input().split())

namoo = list(map(int,input().split()))

print(binary_search(namoo, M))


