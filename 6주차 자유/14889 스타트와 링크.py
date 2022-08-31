

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

#graph = [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
#graph = [[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5], [1, 2, 3, 0, 4, 5], [1, 2, 3, 4, 0, 5], [1, 2, 3, 4, 5, 0]]
#스타트 팀과 링크 팀으로 나누고 거기서 또 2개씩 짝지은 모든 값들을 더해야 함..
#print(graph)
team = [ i+1 for i in range(N)]
start_team = [0 for _ in range(N//2)]
answer = []

def choose_team(start,lst,idx):
    if lst[-1] != 0:
        power1 = 0
        power2 = 0
        for j in lst:
            for k in lst:
                power1 += graph[j-1][k-1]
        
        link_team = list(set(team) - set(lst))
        for j in link_team:
            for k in link_team:
                power2 += graph[j-1][k-1]
        #print(lst, link_team)
        answer.append(abs(power1-power2))
        return

    for i in range(start,N+1):
        lst[idx] = i
        choose_team(i+1,lst,idx+1)
        lst[idx] = 0
        
 
choose_team(1,start_team,0)

print(min(answer))

