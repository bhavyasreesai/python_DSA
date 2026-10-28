def sort(nums):
    n=len(nums)
    if n<=1:
        return nums
    mid=n//2
    left=nums[:mid]
    right=nums[mid:]
    left=sort(left)
    right=sort(right)
    return merge(left, right)
def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
            result.append(left[i])
            i+=1
    while j<len(right):
            result.append(right[j])
            j+=1
    return result
nums=[5,3,7,2,7,3,5,2,8,9,4,5]
print(sort(nums))
#output-[2, 2, 3, 3, 4, 5, 5, 5, 7, 7, 8, 9]
#time complexity-o(nlogn)
#space complexity-o(n)

#note:/=floating value
#//=integer value