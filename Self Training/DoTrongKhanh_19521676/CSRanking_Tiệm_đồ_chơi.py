def twoSum(nums, target):
        numIndex = dict()
        for i in range(len(nums)):
            n = nums[i]
            n2 = target - n
            if n2 in numIndex:
                return [numIndex[n2]+1,i+1]
            numIndex[nums[i]] = i
        return None
n=int(input())
arr=[]
for i in range(0,n):
    m=int(input())
    n1=int(input())
    arr=list(map(int, input().strip().split()))[:n1]
    if len(arr)<2:
        print(*[0,0])
    else:
        s=twoSum(arr,m)
        if s!=None:
            print(*s)
        else:
            print(*[0,0])
