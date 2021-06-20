import sys

def lcs2(a,b):
    import numpy as np
    dp = np.zeros((len(a)+1, len(b)+1)) 
    
    for i,number1 in enumerate(a):   
        for j,number2 in enumerate(b):
            if number1 == number2:   
                dp[i+1][j+1] = dp[i][j]+1
            else:  
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return int(dp[len(a)][len(b)])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
