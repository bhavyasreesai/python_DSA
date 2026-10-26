#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def max(nums,k):
    window ={}
    n=len(nums)
    i=0
    zeros=0
    max_length=0
    for j in range(n):
        if nums[j]==0:
            zeros+=1
        while zeros>k:
            if nums[i]==0:
                zeros-=1
            i+=1
        length=j-i+1
        if length>max_length:
            max_length=length
    return max_length
nums = [1,1, 1,0, 0, 0,1, 1, 1, 1, 0]
k = 2
print(max(nums,k))
#output-6
#time complexity-o(n)
#space complexity-o(1)