from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1  
    elif x + y < y + x:
        return 1   
    else:
        return 0



    
def solution(numbers):
    numbers_str = [str(w) for w in numbers]
    numbers_str.sort(key=cmp_to_key(compare))
    answer = ''
    for i in numbers_str:
        answer += i
    return '0' if answer[0] == '0' else answer