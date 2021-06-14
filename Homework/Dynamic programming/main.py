n, w = input().split()
lst = []
for i in range(int(n)):
    ni = [int(i) for i in input().split()[:2]]
    lst.append(ni)

def KS(n, w, lst):
    if (n == 0) or (w == 0):
        return 0
    elif (lst[n-1][0] > w):
        return KS(n-1, w, lst)
    else:
        return max(lst[n-1][1] + KS(n-1, w-lst[n-1][0], lst), KS(n-1, w, lst))

print(KS(int(n), int(w), lst))