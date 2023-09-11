lt1 = []

for i in range(9):
  lt1.append(list(map(int, input().split())))

x = 0
y = 0
max = -1

for i in range(9):
  for j in range(9):
    if lt1[i][j] > max:
      max = lt1[i][j]
      x = i + 1
      y = j + 1

print(max)
print(x, y)