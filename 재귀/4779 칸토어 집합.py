

def cal(lst, num_start,num_end):
    new_num = num_end//3
    if new_num == 0:
        return 
    
    for i in range(num_start + new_num, num_start + new_num*2):
        lst[i] = ' '
    
    cal(lst,num_start,new_num)
    cal(lst,num_start+new_num*2, new_num)
    



while 1:
    try:
        N = int(input())
        if N == ' ':
            break
        num = 3**N
        lst = ['-' for _ in range(num)]
        cal(lst, 0, num)
        print("".join(lst))
    except EOFError:
        break

