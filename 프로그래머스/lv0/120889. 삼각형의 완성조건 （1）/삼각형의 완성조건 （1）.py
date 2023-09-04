def solution(sides):
    a = []
    a.append(max(sides))
    sides.remove(max(sides))
    a.append(sum(sides))
    
    if a[0] < a[1]:
        return 1
    else:
        return 2