def find(a, x):
    if a[x] == x:
        return x
    a[x] = find(a, a[x])
    return a[x]


def union(a, x, y, fun_smaller=lambda i, j: i < j):
    i = find(a, x)
    j = find(a, y)
    if i == j:
        return
    if fun_smaller(i, j):
        (i, j) = (j, i)
    a[i] = j
