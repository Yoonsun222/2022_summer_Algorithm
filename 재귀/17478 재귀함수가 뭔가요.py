N = int(input())+1



def end(n):
    end_text = '''라고 답변하였지.'''
    print('____'* (N-n) + end_text)
    if n == N:
        return 0
    return end(n+1)


def cal(n):
    start_text = '''"재귀함수가 뭔가요?"'''
    main_tex1 = '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'''
    main_tex2 = '''마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'''
    main_tex3 = '''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''

    
    return_text = '''"재귀함수는 자기 자신을 호출하는 함수라네"'''
    

    print('____'*(N-n) + start_text)


    if n == 1:
        print('____'*(N-n)+ return_text)
        return end(n)
    else:
        print('____'*(N-n) + main_tex1)
        print('____'*(N-n) + main_tex2)
        print('____'*(N-n) + main_tex3)


    return cal(n-1)

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
cal(N)