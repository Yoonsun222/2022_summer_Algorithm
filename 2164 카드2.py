from collections import deque


N = int(input())

stack = deque()

for i in range(1, N+1):
    stack.append(i)


while 1<len(stack):
    stack.popleft()
    cnum = stack.popleft()
    stack.append(cnum)
    # print(stack)

print(stack[0])