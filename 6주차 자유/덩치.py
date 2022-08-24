import sys
input = sys.stdin.readline

N = int(input())

lst = []


for _ in range(N):
    weight, height = map(int,input().split())
    lst.append([weight,height])

for weight , height in lst:
    rank = 1
    for w, h in lst:
        if w > weight and h > height:
            rank += 1
    print(rank, end=' ')
