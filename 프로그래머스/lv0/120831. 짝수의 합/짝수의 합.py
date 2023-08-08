def solution(n):
    answer = 0
    for kk in range(n+1):
        if kk % 2 == 0:
            answer += kk
    return answer