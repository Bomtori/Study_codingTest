time = int(input())
lt1 = list(map(int, input().split()))
M = max(lt1)

lt2 = []
for i in lt1:
    lt2.append(i/M*100)
avg = sum(lt2)/time
print(avg)