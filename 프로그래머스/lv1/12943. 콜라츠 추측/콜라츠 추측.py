def solution(num):
    answer = count = 0
    
    while True:
        if num == 1:
            break
        elif num % 2 == 0:
            num /= 2
            answer += 1
        else:
            num *= 3
            num += 1
            answer += 1
        
        count += 1
        if count >= 500:
            break
        
    if answer >= 500:
        return -1
    else:
        return answer