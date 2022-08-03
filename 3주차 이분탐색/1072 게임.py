import math


def binary_search(X,Y,cur_win_rate):
    
    if cur_win_rate >= 99:
        return -1
    
    start = 0
    end = X

    while start <= end:
        mid = (end + start) // 2
        M = mid
        target = math.trunc((Y+M)*100/(X+M))-1
        #print(target, cur_win_rate,M, start, end)
        
        if cur_win_rate > target:
            start = mid + 1
        else:
            end = mid - 1
    
    return start



X, Y = map(int,input().split())

cur_win_rate = math.trunc(Y*100/X)

print(binary_search(X,Y,cur_win_rate))