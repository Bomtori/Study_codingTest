def solution(x):
    x = str(x)
    lt1 = []
    for a in x:
        b = int(a)
        lt1.append(b)
        
    x = int(x)
    
    if x % sum(lt1) == 0:
        return True
    else:
        return False