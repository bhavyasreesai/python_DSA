def selection_sort(nums):
    n=len(nums)
    for i in range(n-1):
        min_pos=i
        for j in range(i+1,n):
            if nums[j]<nums[min_pos]:
                min_pos=j
        temp=nums[i]
        nums[i]=nums[min_pos]
        nums[min_pos]=temp
        #print(nums)
    return nums
nums=[3,5,3,8,6,7,2]
print(selection_sort(nums))
#output-[2, 3, 3, 5, 6, 7, 8]
#print(nums)
#[2, 5, 3, 8, 6, 7, 3]
#[2, 3, 5, 8, 6, 7, 3]
#[2, 3, 3, 8, 6, 7, 5]
#[2, 3, 3, 5, 8, 6, 7]
#[2, 3, 3, 5, 7, 8, 6]
#[2, 3, 3, 5, 7, 6, 8]
#time complexity-o(n^2)
#space complexity-o(1)
