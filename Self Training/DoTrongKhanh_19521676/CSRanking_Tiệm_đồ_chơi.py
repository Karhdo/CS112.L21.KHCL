def Sum_two(nums, target):
        Num_index = dict()
        for i in range(len(nums)):
            n = nums[i]
            n2 = target - n
            if n2 in Num_index:
                return [Num_index[n2]+1,i+1]
            Num_index[nums[i]] = i
        return None

n = int(input())
lst = []
for i in range(0,n):
    m = int(input())
    n1 = int(input())
    lst = list(map(int, input().strip().split()))[:n1]
    if len(lst) < 2:
        print(*[0,0])
    else:
        s = Sum_two(lst,m)
        if s != None:
            print(*s)
        else:
            print(*[0,0])
