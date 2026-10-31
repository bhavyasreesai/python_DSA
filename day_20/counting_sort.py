def sort(nums):
    n=len(nums)
    max=nums[0]
    for i in range(n):
        if nums[i]>max:
            max=nums[i]
    count=[0]*(max+1)
    for i in range(n):
        count[nums[i]]+=1
    index=0
    for i in range(len(count)):
        while count[i]>0:
            nums[index]=i
            index+=1
            count[i]-=1
    return nums
nums = [4, 2, 2, 1, 3, 4, 1]
print(sort(nums))
#output-[1, 1, 2, 2, 3, 4, 4]
#time complexity-o(n)
#space complexity-o(1)
