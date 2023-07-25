def solution(n):
    answer = 0
    
    for kk in range(n):
        kk += 1
        if n % kk == 1:
            answer = kk
            break
    return answer