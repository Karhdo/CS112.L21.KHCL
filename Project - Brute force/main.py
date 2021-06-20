A = list(map(int, input().strip().split()))
B = []
C = []

res = 0

for i in range(len(A)):
  if A[i] < 0: B.append(A[i])
  if A[i] > 0: C.append(A[i])
  B.sort()
  C.sort()

x = len(B)
y = len(C)

if x >= 2:
  if len(B) % 2 == 0:
    res = max(B[x-1]*B[x-2]*C[y-1], C[y-1]*C[y-2]*C[y-3])
else:
  res = C[y-1]*C[y-2]*C[y-3]
print(res)