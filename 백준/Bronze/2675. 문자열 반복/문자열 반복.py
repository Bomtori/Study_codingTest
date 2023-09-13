time = int(input())
lt1 = []
lt2 = []
for i in range(time):
    lt1 = input().split()
    for j in lt1[1]:
        lt2.append(j*int(lt1[0]))
    
    print(''.join(lt2))
    lt2 = []