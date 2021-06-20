n = int(input())
arr = [int(i) for i in input().split()]
arr_tam1 = []
arr_tam2 = []
for i in range(n):
    if arr[i] not in arr_tam1:
        arr_tam2.append(arr.count(arr[i]))
        arr_tam1.append(arr[i])

#print(arr_tam1, end = " ")
#print(arr_tam2, end = " ")     
    
max_ = max(arr_tam2)
index = arr_tam2.index(max_)
max_kq = arr_tam1[index]
for i in range(len(arr_tam2)):
    if arr_tam2[i] == max_:
        if arr_tam1[i] < max_kq:
            max_kq = arr_tam1[i]
print(max_kq)
