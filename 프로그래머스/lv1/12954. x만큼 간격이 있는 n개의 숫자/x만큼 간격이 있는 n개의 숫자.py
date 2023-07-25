def solution(x, n):
    answer = []
    a = x
    for kk in range(n):
        answer.append(x)
        x += a
    return answer