def max_avg_subarray(nums,k):
    n=len(nums)
    current_sum=0
    for i in range(k):#n
        current_sum+=nums[i]
    max_sum=current_sum
    for i in range(k,n):#n
        current_sum=current_sum-nums[i-k]+nums[i]
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum/k
nums=[1,12,-5,-6,50,3]
k=3
print(max_avg_subarray(nums,k))
#output
#15.666666
#time complexity-o(2n)=o(n)
#space complexity-o(1)
