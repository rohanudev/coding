
def solution(n, w, num):
    answer = 0
    block = [[],[],[],[],[],[],[],[],[],[]]
    answer_col = 0
    answer_row = 0
    
    for i in range(1,n+1):
        if ((i-1)//w)%2 == 0:
            rev = False
        else:
            rev = True
        
        if rev:
            locate = w - ((i-1) % w) - 1
            block[locate].append(i)
            if i == num:
                answer_col = locate
                answer_row = len(block[locate]) - 1
        else:
            locate = (i-1) % w
            block[locate].append(i)
            if i == num:
                answer_col = locate
                answer_row = len(block[locate]) - 1
        
    answer = len(block[answer_col]) - answer_row
    return answer