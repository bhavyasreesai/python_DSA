def sort(nums,k):
    n=len(nums)
    for i in range(k):#range(k) when you only need the K smallest elements. Use range(n-1) when you want to perform a complete Selection Sort.
        min_pos=i
        for j in range(i+1,n):
            if nums[min_pos]>nums[j]:
                min_pos=j
        temp=nums[i]
        nums[i]=nums[min_pos]
        nums[min_pos]=temp
    return nums[:k]#start with 0(default),end with k
nums=[5,3,8,6,7,2]
k=3
print(sort(nums,k))
#output-[2, 3, 5]
#time complexity-o(nk)
#space complexity-(1)