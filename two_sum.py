# 1 question
def two_sum(nums, target) :
    n=len(nums) #to find the length of array
    for i in range(n):
              # here n is stop value and default will be 0
        for j in range(i+1,n):
            # here i+1 is start value and stop is n, so we will start from i+1 and we stop at n
            if nums[i]+nums[j]==target:
                return [i,j]
            #here we only return i,j so only index will return
    return -1
nums = [2,7,8,9]
target = 9
print(two_sum(nums,target))

# time complexity - we have 2 loops so n*n=o(n^2)
# space complexity -we have fixed variables only






