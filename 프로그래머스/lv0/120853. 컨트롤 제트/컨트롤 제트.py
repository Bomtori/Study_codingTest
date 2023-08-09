def solution(s):
    s = list(s.split())
    result = []
    
    i = 0
    while i < len(s):
        if s[i] == 'Z':
            if i > 0:
                result.pop()
        else:
            result.append(s[i])
        i += 1
    return sum(map(int, result))
    