def code():
    a=[102,118,130,145,160,177,190,204,230]
    q=177
    lo=0
    hi=len(a)-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if a[mid]==q:
            return mid
        elif a[mid]<q:
            lo=mid+1
        else:
            hi=mid-1
    return -1
print(code())
