def solution(phone_number):
    answer = ''
    
    for kk in phone_number:
        if len(answer) >= len(phone_number) - 4:
            answer += kk
        else:
            answer += '*'
            
         
        
    return answer