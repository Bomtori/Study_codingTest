def solution(numbers):
    answer = -1
    numbers.sort()
    arr = [0,1,2,3,4,5,6,7,8,9]
    for kk in numbers:
        if kk in arr:
            arr.remove(kk)
    answer = sum(arr)
        
    
    
    return answer