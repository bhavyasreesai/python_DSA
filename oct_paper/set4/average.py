def strong_average(nums,k,T):
    n=len(nums)
    count=0
    for i in range(n-k+1):
        total=0
        for j in range(i,i+k):
            total+=nums[j]
        if total>=k*T:
            count+=1
    return count

nums=[2,2,2,2,5,5,5,8]
k=3
T=4
print(strong_average(nums,k,T))
