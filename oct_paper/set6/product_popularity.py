def code():
    nums=[4,4,6,2,2,2,6,9,6]
    n=len(nums)
    freq={}
    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]]+=1
        else:
            freq[nums[i]]=1
    items=[]
    for x in freq:
        items.append([x,freq[x]])
    def merge_sort(a):
        if len(a)<=1:
            return a
        mid=len(a)//2
        left=merge_sort(a[:mid])
        right=merge_sort(a[mid:])
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i][1]<right[j][1] or (left[i][1]==right[j][1] and left[i][0]>right[j][0]):
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
    items=merge_sort(items)
    result=[]
    for i in range(len(items)):
        for j in range(items[i][1]):
            result.append(items[i][0])
    return result
print(*code())
