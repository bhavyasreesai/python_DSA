#using for loop
def reverse_array(nums):
    n=len(nums)
    for i in range (n//2): # we use n//2 because it will divide the array to half, the loop performs half the swaps
        temp = nums[i]
        nums[i]=nums[n-i-1]
        nums[n-i-1]=temp
    return nums

nums=[1,2,3,4,5]
print(reverse_array(nums))
#time complexity - o(n)
# space complexity - o(1)

#using while loop
def reverse_array(nums):
    n= len(nums)
    left=0
    right=n-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums
nums=[1,2,3,4,5]
print(reverse_array(nums))
#time complexity - o(n)
#space complexity - o(1)

