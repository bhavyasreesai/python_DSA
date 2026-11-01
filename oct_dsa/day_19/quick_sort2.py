#lomuto partition
def sort(nums,low,high):
    pivot=nums[high]
    i=low-1
    for j in range(low,high):
        if nums[j]<=pivot:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
    nums[i+1],nums[high]=nums[high],nums[i+1]
    return i+1
def quick_sort(nums,low,high):
    if low<high:
        s=sort(nums,low,high)
        quick_sort(nums,low,s-1)
        quick_sort(nums,s+1,high)
nums=[8, 3, 1, 7, 0, 10, 2]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
#output-[0, 1, 2, 3, 7, 8, 10]