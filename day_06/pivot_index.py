def pivot_element(nums):
    n=len(nums)
    for i in range(n):
        left=0
        right=0
        for j in range(i):
            left=left+nums[j]
        for j in range(i+1,n):
                right=right+nums[j]
        if left==right:
            return i
    return -1
nums=[1,7,3,6,5,6]
print(pivot_element(nums))
#time complexity-o(n^2)
#space complexity-o(n)

# optimized code
def pivot_element(nums):
    n=len(nums)
    total=0
    left=0
    for i in range(n):
        total=total+nums[i]
    for i in range(n):
        right =total -left-nums[i]
        if left==right:
            return i
        left = left+nums[i]
    return -1
nums=[1,7,3,6,5,6]
print(pivot_element(nums))
#time complexity-o(n)
#space complexity-o(1)
