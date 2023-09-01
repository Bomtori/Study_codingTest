def solution(n, k):
    answer = 0
    a = 0
    for i in range(n):
        answer += 12000
        a += 1
        if a == 10:
            k -= 1
            a = 0
    
    k *= 2000
    answer += k
    return answer