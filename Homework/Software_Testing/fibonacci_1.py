mod = (10**9 + 7)
def fibonacci_1 (n, k):
	arr = [0]*(2*k + 2)
	arr[1] = 1
	for i in range (2, 2*k+2): 
		arr[i] = ((arr[i-1] % mod) + (arr[i-2] % mod)) % mod
	return ((n * arr[2*k+1]) % mod)
