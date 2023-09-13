from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
a = input()
result = []
for i in alphabet_list:
    if i in a:
        result.append(str(a.index(i)))
    elif i not in a:
        result.append('-1')

answer = ' '.join(result)
print(answer)