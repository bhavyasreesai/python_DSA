def card(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return i,j
nums=[120,45,80,200,35,150]
target=235
print(card(nums,target))

#optimal
def card(nums,target):
    seen={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in seen:
            return seen[complement],i
        seen[nums[i]]=i
nums=[120,45,80,200,35,150]
target=235
print(card(nums,target))