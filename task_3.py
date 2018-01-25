
f =[]
y = 1
l = 0
a = [70, 8, 20, 1, 13]
for i in a:
    y = 1
    if len(str(i)) >= 2:
        l = len(str(i)) - 1
        for x in range(l):
            y *= 10
        f.append(int(i) / y)
    else:
        f.append(i)

f.sort()
n = sorted(f)
n.reverse()
k = []
for i in n:
    y = 1
    if len(str(i)) >= 2:
        l = len(str(i)) - 2
        for x in range(l):
            y *= 10
        k.append(int(float(i) * y))
    else:
        k.append(i)
for i in range(len(k)):
    print (k[i], end='')
print()








