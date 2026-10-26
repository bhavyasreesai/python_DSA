def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    return nums
nums=[5,1,34,4,2,8]
print(bubble_sort(nums))
#output-[1, 2, 4, 5, 8, 34]
#time complexity-o(n^2)
#space complexity-o(1)
