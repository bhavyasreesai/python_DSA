def countSubstrings(s):
    count=0
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            left=i
            right=j
            is_palindrome=True
            while left<right:
                if s[left]!=s[right]:
                    is_palindrome=False
                    break
                else:
                    left+=1
                    right-=1
            if is_palindrome:
                count+=1
    return count
print(countSubstrings("aaa"))
#output-6
#time complexity-o(n^3)
#space complexity-o(1)



#optimal
def substring(s):
    n= len(s)
    count=0
    for i in range(n):
        left=i
        right=i
        while left>=0 and right <n and s[left]==s[right]:
            count+=1
            left-=1
            right+=1
        left=i
        right=i+1
        while left>=0 and right<n and s[left]==s[right]:
            count+=1
            left-=1
            right+=1
    return count
s="aaa"
print(substring(s))
#output-6
#time complexity-o(n^2)
#space complexity-o(1)