def solution(absolutes, signs):
    lt1 = []
    for kk in range(len(signs)):
        if signs[kk] == False:
            absolutes[kk] = -absolutes[kk]
            
    return sum(absolutes)