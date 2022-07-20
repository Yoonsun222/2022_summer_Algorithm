
import sys 
input = sys.stdin.readline().rstrip()


N = int(input())

answer= 0
for _ in range(N):
    word = list(input())
    stack = []
    #print(word)
    if len(word) % 2:
        continue
    while word:
        cn = word.pop()
        #print(word ,stack, cn)
        if stack and stack[-1] == cn:
            stack.pop()
        else:
            stack.append(cn)

    if stack:
        continue
    else:
        answer += 1
        
        

print(answer)