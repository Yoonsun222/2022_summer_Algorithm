## 풀이 1

k = int(input())


def wornl1(cnt,start):

    if cnt == k: 
        return start

    answer = []
    for j in range(3):
        for st in start:
            if j == 1:
                answer.append(st + ' ' * cnt+ st)
            else:
                answer.append(st * 3)
    
    return wornl1(cnt*3,answer)
 


start = ['***','* *', '***']
if k == 3:
    for ans in start:
        print(ans)

else:
    answer = wornl1(3,start)
    for ans in answer:
        print(ans)



## 풀이 2


k = int(input())



def wornl1(cnt):

    if cnt == 3: 
        return ['***','* *', '***']

    lines = wornl1(cnt//3)
    answer = []
    for j in range(3):
        for line in lines:
            if j == 1:
                answer.append(line + ' ' * (cnt//3) + line)
            else:
                answer.append(line * 3)
    
    return answer
 


answer = wornl1(k)
for ans in answer:
    print(ans)
