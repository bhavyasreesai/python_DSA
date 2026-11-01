def min_subarray_sum(nums,target):
    n=len(nums)
    i=0
    total=0
    min_length=float('inf')
    for j in range(n):
        total +=nums[j]
        while total>=target:
            length=j-i+1
            if length<min_length:
                min_length=length
            total-=nums[i]
            i+=1
    if min_length==float('inf'):
        return 0
    return min_length
nums=[2,3,1,2,4,3]
target=7
print(min_subarray_sum(nums,target))
#output
#2
#time complexity-o(n)
#space complexity-o(1)


