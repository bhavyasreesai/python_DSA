#brute force
def reverseVowels(s):
    vowels="aeiouAEIOU"
    vowel_string=""
    for ch in s:
        if ch in vowels:
            vowel_string=vowel_string+ch
    rev=""
    for i in range(len(vowel_string) - 1, -1, -1):
        rev=rev+vowel_string[i]
    result=""
    j=0
    for ch in s:
        if ch in vowels:
            result=result+rev[j]
            j+=1
        else:
            result=result+ch
    return result
s = "hello"
print(reverseVowels(s))

#optimal
def reverseVowels(s):
    vowels= "aeiouAEIOU"
    result=""
    left=0
    right=len(s)-1
    while left<=right:
        if s[left] in vowels:
            if s[right] in vowels:
                result=result+s[right]
                right-=1
                left+=1
            else:
                result=result+s[left]
                left+=1
                right-=1
        else:
            result=result+s[left]
            left+=1
    return result
