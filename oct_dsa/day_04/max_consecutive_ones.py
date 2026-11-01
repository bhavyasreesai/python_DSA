def max_consecutive_ones(nums):
    n=len(nums)
    count=0
    max_count=0
    for i in range(n):
        if nums[i]==1:
            count+=1
        else:
            count=0
        if count>max_count:
            max_count=count
    return max_count
nums=[1,1,0,1,1,1]
print(max_consecutive_ones(nums))
#time complexity-o(n) the execution time of an algorithm grows as the input size grows
#space complexity-o(1) the memory required by an algorithm grows as the input size increases

