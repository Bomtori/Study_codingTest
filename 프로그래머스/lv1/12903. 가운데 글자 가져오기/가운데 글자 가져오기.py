def solution(s):
    answer = ''
    b= 0
    if len(s) % 2 == 1:
        a = int(len(s) / 2)
        answer = s[a]
    else:
        a = int(len(s) / 2)
        b += a - 1
        answer = s[b] + s[a]
            
    return answer