
n = int(input())

answer = 0

def mem(n,t_sum):
    global answer

    if n == t_sum:
        answer += 1
        return
    if n < t_sum:
        return

    for i in range(1,4):
        mem(n,t_sum+i)


    return

for _ in range(n):
    num = int(input())
    answer = 0
    mem(num,0)
    print(answer)