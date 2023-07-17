lt1 = []
for kk in range(9):
    a = int(input())
    lt1.append(a)

max1 = max(lt1)
max2 = lt1.index(max(lt1)) + 1

print(max1)
print(max2)
