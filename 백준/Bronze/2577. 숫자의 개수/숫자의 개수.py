lt1 = []
result = 0
for i in range(3):
    lt1.append(int(input()))
    
result += lt1[0] * lt1[1] * lt1[2]
result = str(result)
lt2 = []

for i in result:
    lt2.append(int(i))

for i in range(10):
   print(lt2.count(i))
        