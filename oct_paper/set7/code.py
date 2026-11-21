def code():
    a=[0,0,0,0,0,0,1,1,1,1]
    lo=0
    hi=len(a)-1
    ans=-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if a[mid]==1:
            ans=mid+1
            hi=mid-1
        else:
            lo=mid+1
    return ans
print(code())
