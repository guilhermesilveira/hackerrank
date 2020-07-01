def divisivel_array_elemento(lista, x):
    for y in lista:
        if x % y != 0:
            return False
    return True


def divisivel_elemento_array(x, lista):
    for y in lista:
        if y % x != 0:
            return False
    return True


def getTotalX(a, b):
    entre = 0
    for x in range(max(a), min(b) + 1, max(a)):
        if not divisivel_array_elemento(a, x):
            continue
        if not divisivel_elemento_array(x, b):
            continue
        entre += 1
        # print(x)
    return entre


print(getTotalX([2, 6], [24, 36]))
print(getTotalX([2, 4], [16, 32, 96]))
print(getTotalX([2], [100]))
print(getTotalX([1], [100]))
print(getTotalX([100], [100]))
