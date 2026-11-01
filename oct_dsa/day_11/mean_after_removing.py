
def mean_after_removing(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    remove=n//20
    total=0
    for i in range(remove,n-remove):
        total+=nums[i]
    count=n-2*remove
    return total/count
nums = [1, 2, 36, 8, 6, 0, 3]
print(mean_after_removing(nums))
#output
#8.0
#time complexity-o(n^2)
#space complexity-o(1)
