def longest_unique(nums):
    n=len(nums)
    max_len=0
    for i in range(n):
        seen=[]
        count=0
        for j in range(i,n):
            if nums[j] in seen:
                break
            seen.append(nums[j])
            count+=1
        if count>max_len:
            max_len=count
    return max_len

nums=[12,7,9,4,5,3,12,6,8,2]
print(longest_unique(nums))
