def reverse_string(s):
    n=len(s)
    left= 0
    right=n-1
    while left<right:
        temp=s[left]
        s[left] =s[right]
        s[right]=temp
        left+=1
        right-=1
    return s
s = ["h", "e", "l", "l", "o",1,2,3]
print(reverse_string(s))