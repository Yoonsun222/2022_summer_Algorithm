import sys 
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    imp = deque(map(int,input().split()))
    orgin_index_lst = deque()
    orgin_index_dic = {}  
    for i in range(N):
        orgin_index_dic[chr(65+i)] = 0
        orgin_index_lst.append(chr(65+i))
    
    cnt = 1
    answer_alpha = orgin_index_lst[M]

    while imp:
        max_val = max(imp)
        cn = imp.popleft()
        ca = orgin_index_lst.popleft()

        if max_val == cn:
            orgin_index_dic[ca] = cnt
            cnt += 1
        else:
            imp.append(cn)
            orgin_index_lst.append(ca)

        # print(imp, orgin_index_lst)
    print(orgin_index_dic[answer_alpha])