from collections import deque, defaultdict
n = int(input())
leaf = [1]



is_child = defaultdict(int)
child = defaultdict(list)



#부모노드 할당 및 tree 집어넣기
for _ in range(n-1):
    p,c,v = map(int,input().split())
    child[c].append([p,v])
    child[p].append([c,v])
    is_child[p] = 1

# is_child = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
# child = {2: [[1, 3], [4, 5]], 1: [[2, 3], [3, 2], [2, 3]], 3: [[1, 2], [5, 11], [6, 9]], 4: [[2, 5], [7, 1], [8, 7]], 5: [[3, 11], [9, 15], [10, 4]], 6: [[3, 9], [11, 6], [12, 10]], 7: [[4, 1]], 8: [[4, 7]], 9: [[5, 15]], 10: [[5, 4]], 11: [[6, 6]], 12: [[6, 10]]}

#말단노드 찾기
for i in range(1,n+1):
    if is_child[i]:
        continue
    leaf.append(i)
    
def dfs(node):
    visited = [0 for _ in range(n+1)]
    queue = deque([[node, 0]])
    answer_val = 0
    while queue:
        node,val = queue.popleft()
        visited[node] = 1
       
        answer_val = max(answer_val,val)
        if answer_val == val:
            answer_node = node
        
        for nd,ndv in child[node]:
            if visited[nd] == 1:
                continue
            queue.append([nd,ndv+val])


    return answer_node, answer_val

            
ans = 0

answer_node, answer_val = dfs(1)
answer_node, answer_val = dfs(answer_node)

print(answer_val)