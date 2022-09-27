# #방법 1
# import itertools

# numbers = [ int(input()) for _ in range(9)]


# comb = itertools.combinations(numbers,7)

# for numb in comb:
#     if sum(numb) == 100:
#         for i in numb:
#             print(i)


# 방법2

# numbers = [ int(input()) for _ in range(9)]
# state = True
# sum_numb = sum(numbers)
# for i in range(9):
#     for j in range(i+1,9):
#         sn = sum_numb-numbers[i]-numbers[j]
#         if sn == 100:
#             numbers.pop(j)
#             numbers.pop(i)
#             state = False
#             break
#     if state == False:
#         break

# for i in numbers:
#     print(i)

