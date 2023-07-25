def solution(n):
    n_str = str(n)
    answer = 0

    for kk in n_str:
        answer += int(kk)

    return answer