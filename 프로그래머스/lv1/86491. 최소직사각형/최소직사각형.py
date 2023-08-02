import numpy as np

def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
            
    sizes = np.array(sizes).flatten().tolist()
    max1 = max(sizes[::2])
    max2 = max(sizes[1::2])
    answer += max1 * max2
    return answer