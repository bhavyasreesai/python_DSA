def first_non_repeating_element(nums):
    count={}
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num] =1
    for num in nums:
        if count[num]==1:
            return num
    return None
nums=[4,5,1,2,1,4,5]
print(first_non_repeating_element(nums))
# time complexity - o(n)
# space complexity - o(n)
