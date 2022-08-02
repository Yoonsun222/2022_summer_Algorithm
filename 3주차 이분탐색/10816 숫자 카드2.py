

def binary_search_end(target, array):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid +1
        else:
            end = mid - 1
    
    return end 

def binary_search_start(target,array):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid +1
        else:
            end = mid - 1
    return start

answer = []

N = int(input())
lst1 = list(map(int, input().split()))
lst1.sort()
M = int(input())
lst2 = list(map(int, input().split()))
# print(binary_search(10, lst1)


# N = 10
# lst1 = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
# M = 8
# lst2 = [10, 9, -5, 2, 3, 4, 5, -10]

for num in lst2:
    print(binary_search_end(num, lst1) - binary_search_start(num, lst1) + 1, end = " ")
