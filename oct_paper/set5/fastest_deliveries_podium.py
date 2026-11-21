def code():
    nums=[29,14,36,7,21,14,50]
    k=3
    n=len(nums)
    for i in range(k):
        small=i
        for j in range(i+1,n):
            if nums[j]<nums[small]:
                small=j
        nums[i],nums[small]=nums[small],nums[i]
    result=[]
    for i in range(k):
        result.append(nums[i])
    return result
print(*code())
