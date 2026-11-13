def code(s,p):
    n=len(s)
    m=len(p)
    words=[]
    word=""
    for i in range(n):
        if s[i]!=" ":
            word+=s[i]
        else:
            if word!= "":
                words.append(word)
                word=""
    if word!="":
        words.append(word)
    print(words)
    if len(words)!=m:
        return False
    for i in range(m):
        for j in range(i):
            if p[i]==p[j] and words[i]!=words[j]:
                return False
            if words[i]==words[j] and p[i]!=p[j]:
                return False
    return True
p = "abba"
s = "dog cat cat dog"
print(code(s,p))
#o/p=True
#time com=o(n^2)
#space comp=o(n)