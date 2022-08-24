# 이때에는 한 물통이 비거나, 
# 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.


A, B, C = map(int,input().split())


water = set()

if A > B:
    tmp = B
    B = A
    A = tmp

if A+B >= C and B < C:
    water.add(A)
    water.add(B)
    water.add(C)
    water.add(C-A)
    water.add(C-B)
elif  A+B >= C and B >= C:
    water.add(0)
    water.add(C-A)
    water.add(A)
    water.add(C)
else:
    water.add(C)
    water.add(C-A)
    water.add(C-B)
    water.add(C-B+A)


water = sorted(water)

for ans in water:
    print(ans, end= ' ')