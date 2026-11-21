def code():
    nums=[5,1,4,2,8]
    n=len(nums)
    count=0
    for i in range(n-1):
        flag=0
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=1
        if flag==1:
            count+=1
    print(*nums)
    return count
print(code())
