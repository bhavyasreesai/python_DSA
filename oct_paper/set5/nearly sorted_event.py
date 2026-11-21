def code():
    nums=[10,20,15,30,40,35,50,45]
    n=len(nums)
    count=0
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            count+=1
            j-=1
        nums[j+1]=key
    print(*nums)
    return count
print(code())
