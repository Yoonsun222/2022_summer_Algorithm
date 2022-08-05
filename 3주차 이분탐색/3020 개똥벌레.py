
#석순 종유석 번갈아서

def binary_search(lst,H):
    
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start+end)//2
    
        if lst[mid] <= H:
            start = mid + 1
        else:
            end = mid - 1    
         
    return start

def binary_search2(lst,H):
    
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start+end)//2
    
        if lst[mid] < H:
            start = mid + 1
        else:
            end = mid - 1    
         
    return start




N, H = map(int,input().split())

ss, jy = [], []

for i in range(N):
    num = int(input())
    if i % 2:
        jy.append(num)
    else:
        ss.append(num)

jy.sort()
ss.sort()


# jy = [2, 2, 3, 3, 3, 4, 4] 
# ss = [1, 2, 3, 3, 3, 3, 4]

total_sum = []

for i in range(H):
    total_sum.append(N - (binary_search(ss,i)+binary_search2(jy,H-i)))

min_val = min(total_sum)

print(min_val, total_sum.count(min_val))