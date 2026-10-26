def parity_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if nums[j]%2!=0 and nums[j+1]%2==0:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

    return nums
nums=[7, 4, 5,3,8, 1]
print(parity_sort(nums))
#output-[4, 8, 7, 5, 3, 1]
#time complexity-o(n^2)
#space complexity-o(1)
