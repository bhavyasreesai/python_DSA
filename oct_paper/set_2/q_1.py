def code(nums):
    n=len(nums)
    freq={}
    max=0
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
        if freq[i]>n/2:
            max=i
    return max
nums=[3,2,3,3,1,3,2,3,3]
print(code(nums))
#o/p=3