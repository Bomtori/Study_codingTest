def solution(n):
    answer = -1
    for kk in range(n+1):
        if kk ** 2 == n:
            answer = (kk + 1) ** 2
            break
    return answer