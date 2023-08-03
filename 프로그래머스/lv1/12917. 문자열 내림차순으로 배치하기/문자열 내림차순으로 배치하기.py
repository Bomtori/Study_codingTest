def solution(s):
    answer = sorted(s, reverse = True)
    answer = ''.join(i for i in answer)
    return answer