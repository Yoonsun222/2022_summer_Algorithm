import sys 
input = sys.stdin.readline


T = int(input())


def binary_search(target, array):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid +1
        else:
            end = mid - 1
    return array[end]

for _ in range(T):
    answer = []
    N = int(input())
    lst1 = list(map(int, input().split()))
    lst1.sort()
    M = int(input())
    lst2 = list(map(int, input().split()))

    for num in lst2:
        if num == binary_search(num,lst1):
            print(1)
        else:
            print(0)

