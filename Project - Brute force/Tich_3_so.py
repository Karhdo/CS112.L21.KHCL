a = list(map(int,input().split()))

max = a[0] * a[1] * a[2]

for i in range(len(a)-2):
    for j in range(i + 1, len(a)-1):
        for k in range(j+1, len(a)):
            if a[i] * a[j] * a[k] > max:
                max = a[i] * a[j] * a[k]

print(max)