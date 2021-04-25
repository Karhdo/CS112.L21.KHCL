def divisor_sum(x):
    if (x==1):
        return 0
    sum = 1
    for i in range(2,int(x/2)+1):
        if (x%i) == 0:
            sum += i
    return sum

l = int(input())
r = int(input())
count = 0
for i in range(l,r+1):
    if divisor_sum(i) > i:
        count += 1
print(count)