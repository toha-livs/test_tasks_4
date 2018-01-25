
# вторая задача
d = []
r = []
b = [12, 241, 4, 8]
for i in b:
    if i % 2 == 0:
        r.append(i)
    else:
        d.append(i)
if len(r) > len(d):
    print(d[0])
else:
    print(r[0])


