
def binary_search(lst):
    start = 0
    end = lst[-1] - lst[0]

    while start <= end:
        mid = (start+end)//2
        

N, C = map(int, input().split())

# lst = []
# for i in range(N):
#     lst.append(int(input()))

# lst.sort()

lst = [1, 2, 4, 8, 9]
