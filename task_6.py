# l = d.keys()   ['a', 'b', 'c']


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"sugar": 4030, "eggs": 523, "milk": 20}


def count(a, b):
    result = []
    rec = a.keys()
    for i in range(len(a)):
        for n in rec:
            try:
                x = b[n] / a[n]
                if x >= 1:
                    result.append(x)
                else:
                    return 0
            except KeyError:
                return 0
    result.sort()
    result_1 = sorted(result)
    return int(result_1[0])


print(count(recipe, available))