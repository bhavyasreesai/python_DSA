def max_sum_size(nums,k):
    n=len(nums)
    current_sum=0
    for i in range(k):
        current_sum=current_sum+nums[i]
    max_sum=current_sum
    for i in range(k,n):
        current_sum=current_sum-nums[i-k]+nums[i]
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
nums=[1,12,14,5,9,10]
k=2
print(max_sum_size(nums,k))
#output
#26
#time complexity-o(2n)=o(n)
#space complexity-o(1)
