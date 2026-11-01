def sort(nums,low,high):
    pivot=nums[low]
    x=low
    mid=low
    y=high
    while mid<=y:
        if nums[mid]<pivot:
            nums[x],nums[mid]=nums[mid],nums[x]
            x+=1
            mid+=1
        elif nums[mid]==pivot:
            mid+=1
        else:
            nums[mid],nums[y]=nums[y],nums[mid]
            y-=1
    return x,y
def quick_sort(nums,low,high):
    if low<high:
        x,y=sort(nums,low,high)
        quick_sort(nums,low,x-1)
        quick_sort(nums,y+1,high)
nums=[4, 2, 4, 1, 4, 3, 4, 5]
quick_sort(nums,0,len(nums)-1)
print(nums)

#output-[1, 2, 3, 4, 4, 4, 4, 5]
#time complexity-o(nlogn) avg
#worst case=o(n^2)
#space complexity-o(logn) avg
#worst case-o(n)