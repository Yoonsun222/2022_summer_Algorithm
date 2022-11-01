
from collections import Counter
import sys 


input = sys.stdin.readline 


def cal(N, papers, answer):
    state = False

    a,b,c = 0,0,0

    for j in range(N):
        paper_count = Counter(papers[j])
        a += paper_count[0]
        b += paper_count[1]
        c += paper_count[-1]

    #print(papers)

    # print(N, a, b, c)
    if a == N**2:
        answer[0] +=1
        return
    elif b == N**2:
        answer[1] += 1
        return
    elif c == N**2:
        answer[-1] += 1
        return
    else:
        state = False
    
    if state == False and len(papers) > 1:
        for l in range(0,N,N//3):
            for i in range(0,N,N//3):
                paper = []
                for j in range(0,N//3):
                    paper.append(papers[i+j][l:l+N//3]) 
                cal(N // 3, paper, answer)

N = int(input())
papers = [ list(map(int,input().split())) for _ in range(N)]

answer = {}
for i in range(-1,2):
    answer[i] = 0

# papers = [[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 0, 1, -1, 0, 1, -1], [0, 1, -1, 1, 0, -1, 0, 1, -1]]
 

cal(N, papers, answer)

for i in answer.values():
    print(i)

