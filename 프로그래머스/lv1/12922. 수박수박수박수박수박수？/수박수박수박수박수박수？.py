def solution(n):
    answer = ''
    for kk in range(n):
        if kk % 2 == 1:
            answer += '박'
        else:
            answer += '수'
    return answer