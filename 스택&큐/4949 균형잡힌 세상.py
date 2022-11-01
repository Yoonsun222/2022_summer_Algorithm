

def poppush(lst , i, stack):
    if lst[i] == '(':
        stack.append('(')
    elif lst[i] == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            return False
            
    elif lst[i] == '[':
        stack.append('[')

    elif lst[i] == ']':
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
            


check = [')','(','[',']']

while 1:
    lst = input()
    state = True
    if lst == '.':
        break
    stack = []
    for i in range(len(lst)):
        if lst[i] in check:
            state = poppush(lst, i, stack)
            if state == False:
                break
        
    if stack or state == False:
        print('no')
    else:
        print('yes')
