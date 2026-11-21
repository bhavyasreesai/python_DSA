def code():
    nums=[40,25,60,25,90,75,60,30,50]
    k=3
    n=len(nums)
    target=n-k
    low=0
    high=n-1
    while low<=high:
        pivot=nums[high]
        i=low
        for j in range(low,high):
            if nums[j]<=pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i],nums[high]=nums[high],nums[i]
        if i==target:
            return nums[i]
        elif i<target:
            low=i+1
        else:
            high=i-1
    return -1

print(code())
