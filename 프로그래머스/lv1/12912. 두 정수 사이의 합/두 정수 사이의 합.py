def solution(a, b):
    answer = 0
    if a > b:
        for kk in range(b, a + 1):
            answer += kk
    elif b > a:
        for kk in range(a, b + 1):
            answer += kk
    else:
        answer = a
        
    return answer
