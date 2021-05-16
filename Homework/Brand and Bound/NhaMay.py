nhap = int(input())
a = []
for i in range(nhap):
    v = [int (j) for j in input().split()]
    a.append(v)

def CDi(i, j):
    CD1 = a[i][j]
    for y in range(len(a)):
        if (y != i):
            k = a[y].index(min(a[y]))
            if (k != j):
                CD1 = CD1 + a[y][k]
            else:
                b = a[y].copy()
                b[k] = max(b)
                CD1 = CD1 + min(b)
    return CD1

TTG = 0
next = []
for i in range(len(a)):
    tg0 = []
    cd0 = []
    for j in range(len(a)):
        tg0.append(a[i][j])
        cd0.append(CDi(i, j))

    for k in next:
        cd0[k] = max(cd0)

    CD = min(cd0)
    next.append(cd0.index(CD))
    TTG = TTG + tg0[cd0.index(CD)]

print(TTG)
input()