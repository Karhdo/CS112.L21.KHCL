mod = (10 ** 9 + 7)

def fibo2(k):
    f0 = 0
    f1 = 1
    fn = 1

    if (k <= 1):
        return k
    else:
        for i in range(2, k):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn % mod

def fibonacci_2(n, k):
    return (n * fibo2(2 * k + 1)) % mod


