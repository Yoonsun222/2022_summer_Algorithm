N = int(input())
num = list(map(int,input().split()))
cal = list(map(int,input().split()))


#cal = ['+','-','*','/']
answer = []


def backtracking(idx,ans):
    
    if idx == N:
        answer.append(ans)
        return 
    if cal[0]:
        cal[0] -= 1
        backtracking(idx+1, ans + num[idx])
        cal[0] += 1 

    if cal[1]:
        cal[1] -= 1
        backtracking(idx+1,ans - num[idx])
        cal[1] += 1

    if cal[2]:
        cal[2] -= 1
        backtracking(idx+1, ans * num[idx])
        cal[2] += 1
    if cal[3]:
        cal[3] -= 1
        backtracking(idx+1, int(ans / num[idx]))
        cal[3] += 1


backtracking(1,num[0])

#print(answer)
answer.sort()

print(answer[-1])
print(answer[0])
