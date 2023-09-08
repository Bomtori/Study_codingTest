def solution(n):
    result = 0
    while True:
        if n == 7:
            result += 1
            break
        if n < 7:
            result += 1
            break
        n -= 7
        result += 1
    return result