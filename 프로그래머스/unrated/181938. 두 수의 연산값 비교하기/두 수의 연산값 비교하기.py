def solution(a, b):
    answer = 0
    ans1 = str(a) + str(b)
    ans2 = 2 * a * b
    ans1 = int(ans1)
    answer = max(ans1, ans2)
    return answer