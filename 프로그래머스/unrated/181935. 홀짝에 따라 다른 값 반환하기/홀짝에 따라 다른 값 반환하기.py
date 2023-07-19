def solution(n):
    answer = 0
    if n % 2 == 1:
        for kk in range(n + 1):
            if kk % 2 == 1:
                answer += kk
    else:
        for kk in range(n + 1):
            if kk % 2 == 0:
                answer += kk * kk
        
    return answer