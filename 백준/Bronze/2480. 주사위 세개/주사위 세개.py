#2480번 주사위 세개

d = list(map(int, input().split()))

if d[0] == d[1] == d[2]:
  reward = 10000 + d[0] * 1000
elif d[0] == d[1]:
  reward = 1000 + d[0] * 100
elif d[0] == d[2]:
  reward = 1000 + d[0] * 100
elif d[1] == d[2]:
  reward = 1000 + d[1] * 100
else:
  reward = max(d) * 100

print(reward)