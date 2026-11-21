def code():
    a=[2,5,9,14,20,17,11,6,1]
    h=11
    n=len(a)
    lo=0
    hi=n-1
    while lo<hi:
        mid=lo+(hi-lo)//2
        if a[mid]<a[mid+1]:
            lo=mid+1
        else:
            hi=mid
    peak=lo
    ans=-1
    lo=0
    hi=peak
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if a[mid]==h:
            ans=mid
            hi=mid-1
        elif a[mid]<h:
            lo=mid+1
        else:
            hi=mid-1
    if ans!=-1:
        return ans
    lo=peak+1
    hi=n-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if a[mid]==h:
            return mid
        elif a[mid]<h:
            hi=mid-1
        else:
            lo=mid+1
    return -1
print(code())
