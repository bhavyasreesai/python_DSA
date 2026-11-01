def range_sum_query(nums,left,right):
    total=0
    for i in range(left,right+1):
        total=total+nums[i]
    return total
nums=[-2,0,3,-5,2,-1]
print(range_sum_query(nums,0,2))

#time complexity-o(n)
#space complexity-o(1)