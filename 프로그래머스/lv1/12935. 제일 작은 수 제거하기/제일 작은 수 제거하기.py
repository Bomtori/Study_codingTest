def solution(arr):
    if len(arr) == 1: 
        arr = [-1]
    else: 
        a = min(arr)
        arr.remove(a)
    return arr