#brute force
def isPalindrome(s):
    clean=""
    for ch in s:
        if ch.isalnum():
            clean=clean+ch.lower()
    reverse=""
    for i in range(len(clean)-1,-1,-1):
        reverse=reverse+clean[i]
    if clean==reverse:
        return True
    else:
        return False

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
#output-True
#time complexity-o(n^2)
#space complexity-o(n)

#optimal code
def isPalindrome(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1
        elif s[left].lower()!=s[right].lower():
            return False
        else:
            left+=1
            right-=1
    return True
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
#output-True
#time complexity-o(n)
#space complexity-o(1)
