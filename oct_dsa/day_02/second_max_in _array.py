def second_max_in_array(nums):
    n=len(nums)
    maxi=-1
    second_maxi=-1
    for i in range(n):
        if nums[i]>maxi:
            maxi=nums[i]
    for i in range(n):
        if nums[i]>second_maxi and nums[i]!=maxi:
            second_maxi=nums[i]
    return second_maxi
nums=[20,30,40,50,70,100]
print (second_max_in_array(nums))
# we will traverse array twice
#in first array we will find the largest number
#in the second traversal we will find the largest number by ignoring the largest number in first traversal
#time complexity - o(2n)=o(n)
#space complexity - o(1)