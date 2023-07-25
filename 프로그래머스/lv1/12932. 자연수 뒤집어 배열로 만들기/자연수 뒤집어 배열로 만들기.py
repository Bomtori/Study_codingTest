def solution(n):
    answer = []
    n_str = str(n)
    
    for kk in reversed(n_str):
        answer.append(kk)
        
    answer = [int(kk) for kk in answer]
    
    return answer