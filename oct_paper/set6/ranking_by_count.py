def code():
    nums=[78,92,65,78,100,0,65,92,78,55]
    count=[0]*101
    for i in range(len(nums)):
        count[nums[i]]+=1
    result=[]
    for i in range(101):
        for j in range(count[i]):
            result.append(i)
    return result
print(*code())
