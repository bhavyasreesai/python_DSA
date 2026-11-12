def code(nums):
    result=[]
    count=0
    for i in range(len(nums)):
        if nums[i]!=0:
            result.append(nums[i])
        else:
            count+=1
    for i in range(count):
        result.append(0)
    return result
nums=[0,14,0,3,7,0,0,9,5]
print(code(nums))
#o/p=[14, 3, 7, 9, 5, 0, 0, 0, 0]