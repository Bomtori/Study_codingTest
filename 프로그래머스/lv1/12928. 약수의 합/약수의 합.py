def solution(n):
    answer = 0
    lt1 = []
    for kk in range(n):
        kk += 1
        if n % kk == 0:
            lt1.append(kk)
    answer = sum(lt1)
    return answer