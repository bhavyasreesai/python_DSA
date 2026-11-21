def repeated_login(nums,k):
    n=len(nums)
    for i in range(n):
        for j in range(i):
            if nums[i]==nums[j] and i-j<=k:
                return "YES"
    return "NO"
nums=[7,12,5,7,12,9,12,4]
k=2
print(repeated_login(nums,k))
