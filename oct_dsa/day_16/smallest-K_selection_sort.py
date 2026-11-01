def sort(nums):
    n=len(nums)
    for i in range(n-1):
        min_pos=i
        for j in range(i+1,n):
            if nums[min_pos]>nums[j]:
                min_pos=j
        temp=nums[min_pos]
        nums[min_pos]=nums[j]
        nums[j]=temp
    return nums[j]
nums=[5,1,3,8,6,7,2]
print(sort(nums))
#output-1
#Inside the loop
#Swapping happens before you have finished searching. This can perform unnecessary swaps and is not the standard Selection Sort approach.
#Outside the loop
#Find the smallest element first, then put it in its correct position with one swap per pass. This is standard Selection Sort.
#time complexity-o(n^2)
#space complexity-o(1)
