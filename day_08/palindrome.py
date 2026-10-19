def palindrome(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower()!=s[right].lower():
            return False
        else:
            left+=1
            right-= 1
    return True
s = "racecar"
print(palindrome(s))

#time complexity-o(n)
#space complexity-o(1)