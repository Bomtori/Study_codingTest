time = int(input())
a = b = c = d = 0

while True:
    if time >= 300:
        a += 1
        time -= 100
    elif time >= 60:
        b += 1
        time -= 60
    elif time >= 10:
        c += 1
        time -= 10
    elif time == 0:
        break
    else:
        d = -1
        break

if d == -1:
    print(-1)
else:
    print(f"{a} {b} {c}")