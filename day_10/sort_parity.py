#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

#Return any array that satisfies this condition
def sort_parity(nums):
    n= len(nums)
    j=0
    for i in range(n):
        if nums[i]%2==0:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            j+=1
    return nums
nums = [3,6,1,2,4]
print(sort_parity(nums))

#output
#[6, 2, 4, 3, 1]
#case-2
#if nums[i]%2!=0:
#temp=nums[i]
#nums[i]=nums[j]
#nums[j]=temp
#j+=1
#output
#[3, 1, 6, 2, 4]
#
#time complexity-o(n)
#space complexity-o(1)