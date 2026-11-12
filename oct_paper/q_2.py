def first_duplicate(nums):
    n=len(nums)
    for i in range(n):
        for j in range(i):
            if nums[i]==nums[j]:
                return nums[i]
    return -1
nums=[4021,3377,5120,3377,4021,9001,5120,7]
print(first_duplicate(nums))


