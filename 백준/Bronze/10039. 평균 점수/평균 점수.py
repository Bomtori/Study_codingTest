lt1 = []
lt2 = []
for kk in range(5):
    a = int(input())
    lt1.append(a)

for kk in range(len(lt1)):
    if lt1[kk] < 40:
        lt2.append(40)
    else:
        lt2.append(lt1[kk])

avg = sum(lt2)/len(lt2)
print(int(avg))