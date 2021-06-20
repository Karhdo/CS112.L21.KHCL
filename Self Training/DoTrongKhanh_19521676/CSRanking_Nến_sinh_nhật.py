n = int(input())
lst = [int(i) for i in input().split()]
max_lst = max(lst)
count_max = lst.count(max_lst)
print(count_max)
