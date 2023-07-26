def solution(n):
    answer = 0
    n = str(n)
    lt1 = []
    
    for kk in n:
        lt1.append(int(kk))
        
    lt1.sort(reverse = True)
    
    answer = int(''.join(str(x) for x in lt1))
    
    return answer