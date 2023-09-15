n1 = '' 
n2 = ''
n = list(map(str, input().split()))

for i in reversed(n[0]):
    n1 += i
for i in reversed(n[1]):
    n2 += i
    
if int(n1) > int(n2):
    print(int(n1))
elif int(n1) < int(n2):
    print(int(n2))