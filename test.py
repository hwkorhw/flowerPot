t = ["2020-09-17", "2020", "123"]

t[0] = t[0][2:].split('-')
s = ''.join(t[0])

print(s)