def early_exit(nums):
    n=len(nums)
    for i in range(n):
        swapped=False
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                swapped=True
        if swapped==False:
            break
    return nums
nums = [1,3, 2, 3, 4, 5]
print(early_exit(nums))
#output-[1, 2, 3, 3, 4, 5]
#time complexity-o(n) best case , already sorted
#space complexity-o(1)