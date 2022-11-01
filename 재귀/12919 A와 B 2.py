lst = list(input())

answer_lst = list(input())
answer_len = len(answer_lst)
answer = []



def popAB(answer_lst):
    
    if answer_lst[0] == 'B':
        answer_lst.reverse()
        answer_lst.pop()
        popAB(answer_lst)

        if answer_lst[0] == 'A':
            answer_lst.append('B')
            answer_lst.reverse()
            answer_lst.pop()
        
    else:
        if answer_lst[-1] == 'B':
            return

        answer_lst.pop()
        if answer_lst == lst:
            answer.appepnd(1)
            return
        elif len(answer_lst) < 1:
            return
    
    popAB(answer_lst)
        
popAB(answer_lst)

if answer:
    print(1)
else:
    print(0)


popAB(answer_lst)


# lst = list(input())

# answer_lst = list(input())
# answer_len = len(answer_lst)
# answer = []


# def plusA(lst):
#     lst1, lst2 = lst[:], lst[:]
#     lst1.append('A')
#     lst2.append('B')
#     lst2 = lst2[::-1]
#     #print(lst1,lst2)
#     if lst1 == answer_lst or lst2 == answer_lst:
#         answer.append(1)
#         return
#     elif len(lst1)> answer_len:
#         return 
#     else:
#         plusA(lst1)
#         plusA(lst2)



# plusA(lst)

# if answer:
#     print(1)
# else:
#     print(0)