def code():
    a=[10,20,30,45,60,80]
    t=50
    lo=0
    hi=len(a)-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if a[mid]==t:
            return mid
        elif a[mid]<t:
            lo=mid+1
        else:
            hi=mid-1
    return lo
print(code())
