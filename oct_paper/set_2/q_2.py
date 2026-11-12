def code(nums):
    n= len(nums)
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in nums:
        if freq[i]==1:
            return i
    return -1
nums=17,23,17,8,23,42,8,5,42,17
print(code(nums))
#o/p=5