#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
def square_sorted(nums):
    n=len(nums)
    for i in range(n):
        nums[i]=nums[i]*nums[i]
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums
nums=[-4,-1,0,3,10]
print(square_sorted(nums))
#output
#[0, 1, 9, 16, 100]
#time complexity-o(n^2)
#space complexity-o(1)
#first we will square and then sort