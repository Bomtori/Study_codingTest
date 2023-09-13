lt1 = []
lt2 = []
time = int(input())
for i in range(time):
    lt1.append(input())

for i in range(len(lt1)):
    count = 0
    for j in lt1[i]:
        if j == 'O':
            lt2.append(j)
        elif j == 'X':
            a = lt2.count('O')
            for l in range(a):
                count += l+1
            lt2 = []
    a = lt2.count('O')
    for l in range(a):
            count += l+1
    lt2 = []
    print(count)