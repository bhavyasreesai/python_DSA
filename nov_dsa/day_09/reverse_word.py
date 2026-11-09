#brute force
def reverseWords(s):
    result=""
    word =""
    for i in range(len(s)):
        if s[i]!=" ":
            word=word + s[i]
        else:
            rev=""
            for j in range(len(word)-1, -1, -1):
                rev=rev+word[j]
            result=result+rev+" "
            word=""
    rev=""
    for j in range(len(word)-1, -1, -1):
        rev=rev+word[j]
    result=result +rev
    return result
s = "cat dog"
print(reverseWords(s))
#output-tac god

#optimal
def reverseWords(s):
    result=""
    start=0
    for i in range(len(s) + 1):
        if i==len(s) or s[i]==" ":
            for j in range(i - 1, start - 1, -1):
                result=result + s[j]
            if i<len(s):
                result=result+" "
            start=i+1
    return result
s = "Let's take Python"
print(reverseWords(s))
#output-s'teL ekat nohtyP