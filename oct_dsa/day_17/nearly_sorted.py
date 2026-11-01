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
nums=[1, 2, 4, 3, 5, 6]
print(sort(nums))
#output-[1, 2, 3, 4, 5, 6]
#time complexity-o(n) best
#avg-o(n^2)
#worst-o(n^2)
#space complexity-o(1)