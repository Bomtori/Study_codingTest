def solution(price, money, count):
    a = 0
    for kk in range(count):
        a += price * (kk+1)
    
    if a > money:
        return -1*(money - a)
    else:
        return 0