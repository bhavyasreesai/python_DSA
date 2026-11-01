#Hoare partiation
def sort(nums,low,high):

    pivot=nums[low]
    i=low-1
    j=high+1
    while True:
        i+=1
        while nums[i]<pivot:
            i+=1
        j-=1
        while nums[j]>pivot:
            j-=1
        if i>=j:
            return j
        nums[i],nums[j]=nums[j],nums[i]
def quick_sort(nums,low,high):
    n=len(nums)
    if low<high:
        p=sort(nums,low,high)
        quick_sort(nums,low,p)
        quick_sort(nums,p+1,high)
nums=[3,45,26,7,1,9,6,15,8]
quick_sort(nums,0,len(nums)-1)
print(nums)
#output-[1, 3, 6, 7, 8, 9, 15, 26, 45]
#time complexity-o(nlogn)-best case
# worst case-o(n^2)\
#space complexity-o(logn)
