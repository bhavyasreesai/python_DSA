#brute force
def isPalindrome(x):
    s=str(x)
    reverse= ""
    for i in range(len(s) - 1, -1, -1):
        reverse=reverse+s[i]
    if s==reverse:
        return True
    else:
        return False
print(isPalindrome(121))
#output-True
#time complexity-o(n^2)
#space complexity-o(n)


#optimal
def isPalindrome(x):
    if x <0:
        return False
    original=x
    reverse=0
    while x>0:
        digit=x%10
        reverse=reverse*10+digit
        x=x//10
    return original==reverse
print(isPalindrome(121))
##output-True
#time complexity-o(log n)
#space complexity-o(1)