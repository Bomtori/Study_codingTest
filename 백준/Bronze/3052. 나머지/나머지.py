lt1 = []
lt2 = []
for i in range(10):
    lt1.append(int(input()))

for i in lt1:
    lt2.append(i%42)

result = 0
for i in range(42):
    count = lt2.count(i)
    if count >= 1:
        result += 1

print(result)