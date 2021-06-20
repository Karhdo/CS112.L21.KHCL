import sys

def gcd_naive(a, b):
    m = max(a,b)
    n = min(a,b)
    if m%n ==0 :
        return n
    
    return gcd_naive(n,m%n)
    
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
