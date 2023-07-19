sum = 0
lt1 = []

for kk in range(4):
    a, b = input().split()
    sum += int(b)
    sum -= int(a)
    lt1.append(sum)

max1 = max(lt1)

print(max1)