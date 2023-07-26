def solution(arr, divisor):
    answer = []
    
    for kk in range(len(arr)):
        if arr[kk] % divisor == 0:
            answer.append(arr[kk])
    answer.sort()
    
    if answer == []:
        return [-1]
    return answer