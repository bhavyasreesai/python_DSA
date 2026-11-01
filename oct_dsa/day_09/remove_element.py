
def remove_element(nums, val):
    n=len(nums)
    j=0
    for i in range(n):
        if nums[i]!=val:
            nums[j]=nums[i]
            j+=1
    return j
nums =[3, 2, 2, 3]
val=3
k = remove_element(nums, val)
print(k)
print(nums[:k])
