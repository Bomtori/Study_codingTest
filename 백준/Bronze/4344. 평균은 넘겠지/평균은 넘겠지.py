n = int(input())

for i in range(n):
    lt1 = list(map(int, input().split()))
    avg = sum(lt1[1:])/lt1[0]

    count = 0
    for i in lt1[1:]:
        if i > avg:
            count += 1

    per = (count/lt1[0]) * 100
    print('%.3f' %per + '%')
