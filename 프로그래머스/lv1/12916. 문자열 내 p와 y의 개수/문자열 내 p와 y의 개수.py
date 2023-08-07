def solution(s):
    answer = True
    p = y = 0
    s = s.lower()
    for i in s:
        if 'p' == i:
            p += 1
        elif 'y' == i:
            y += 1
    
    if p == y:
        return True
    elif p != y:
        return False