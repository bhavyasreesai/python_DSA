def remove_duplicates(nums):
    n=len(nums)
    if n==0:
        return 0
    j=1
    for i in range(1,n):
        if nums[i]!=nums[j - 1]:
            nums[j]=nums[i]
            j+=1
    return j
nums = [1, 1, 2, 2, 3]
k = remove_duplicates(nums)
print(k)
print(nums[:k])