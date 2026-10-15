
def disappeared_numbers(nums):
    n=len(nums)
    result=[]
    for i in range(1,n+1):
        found = False
        for j in range(n):
            if nums[j]==i:
                found = True
                break
        if not found:
                result=result+[i]
    return result
nums=[4,3,2,7,8,3]
print(disappeared_numbers(nums))
#time complexity-o(n^2)
#space complexity-o(1)