def solution(seoul):
    for kk in range(len(seoul)):
        if seoul[kk] == "Kim":
            return f"김서방은 {kk}에 있다"