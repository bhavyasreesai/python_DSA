def code(s):
    n=len(s)
    words=[]
    word=""
    for i in range(n):
        if s[i]!=" ":
            word+=s[i]
        else:
            if word!='':
                words.append(word)
                word=""
    if word!="":
        words.append(word)
    return len(words[-1])
s=" hello python "
print(code(s))
#output-6
#time complexity-o(n)
#space complexity-o(n)

#optimal
def code(s):
    n=len(s)
    count=0
    i=n-1
    while i>=0 and s[i]==" ":
        i-=1
    while i>=0 and s[i]!=" ":
        count+=1
        i-=1
    return count
s=" hello python "
print(code(s))
#output-6
#time complexity-o(n)
#space complexity-o(1)

