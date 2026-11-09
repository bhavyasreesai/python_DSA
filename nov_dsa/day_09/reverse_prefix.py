#brute force
def reversePrefix(word, ch):
    index=-1
    for i in range(len(word)):
        if word[i]==ch:
            index=i
            break
    if index == -1:
        return word
    result=""
    for i in range(index,-1,-1):
        result=result+word[i]
    for i in range(index+1,len(word)):
        result=result+word[i]
    return result
word="abcdefd"
ch="d"
print(reversePrefix(word, ch))

#optimal
def reversePrefix(word, ch):
    index=-1
    for i,c in enumerate(word):
        if c==ch:
            index=i
            break
    if index==-1:
        return word
    result=""
    for i in range(index,-1,-1):
        result=result+word[i]
    for i in range(index+1,len(word)):
        result = result+word[i]
    return result
word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))