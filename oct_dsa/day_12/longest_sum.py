#Given an array nums and a number k, find the length of the longest consecutive subarray whose sum is exactly equal to k.
#nums = [1, 2, 1, 1, 1, 3]
#k = 3
def longest_sum(nums,k):
    n=len(nums)
    i=0
    total=0
    max_length=0
    for j in range(n):
        total+=nums[j]
        while total>k:
            total-=nums[i]
            i+=1
        if total==k:
            length=j-i+1
            if length > max_length:
                max_length=length

    return max_length
nums=[1,2,1,1,1,3]
k=3
print(longest_sum(nums,k))
#output
#3
#time complexity-o(n)
#space complexity-o(1)