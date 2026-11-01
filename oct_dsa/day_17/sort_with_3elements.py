def sort(nums):
    n=len(nums)
    for i in range(n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
nums=[2, 0, 1, 2, 1, 0]
print(sort(nums))
#output-[0, 0, 1, 1, 2, 2]
#time complexity-o(n) best
#avg-o(n^2)
#worst-o(n^2)
#space complexity-o(1)
