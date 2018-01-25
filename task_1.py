count = -1
count_2 = -1
count_3 = -1
count_int = []
count_col = []
color = []
integer = []
a = ['yellow', 'white', '2', '5', 'green', 'red', '6', '1']
for i in a:
    count += 1
    if len(i) == 1:
        count_int.append(count)
        integer.append(i)
    elif len(i) >= 2:
        count_col.append(count)
        color.append(i)
color.sort()
integer.sort()
new_color = sorted(color)
new_integer = sorted(integer)
for i in range(1):
    for f in count_col:
        count_2 += 1
        a[f] = new_color[count_2]
    for f in count_int:
        count_3 += 1
        a[f] = new_integer[count_3]
print(a)







