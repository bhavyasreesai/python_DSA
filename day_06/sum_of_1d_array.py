def sum_of_1d_array(nums):
    n=len(nums)
    total=0 #keeping total as 0
    for i in range(n):
        total=total+nums[i]#stored total+element at the index i
        nums[i]=total# now the element at the index i will be replaced by total
    return nums #returning the nums
nums=[1,2,3,4,5]
print(sum_of_1d_array(nums))

#time complexity-o(n) the execution time of an algorithm grows as the input size grows
#space complexity-o(1) the memory of an algorithm takes as the input size grows