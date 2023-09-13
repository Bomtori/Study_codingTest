def solution(n):
    answer = []
    temp = 0
    while True:
        if n >= 3:
            temp = n % 3
            answer.append(temp)
            n = n // 3
            temp = 0
        elif n < 3:
            answer.append(n)
            break
    
    result = 0
    len1 = len(answer)
    for i , j in zip(range(len1), reversed(range(len1))):
        result += answer[i] * 3 ** j
        
    return result