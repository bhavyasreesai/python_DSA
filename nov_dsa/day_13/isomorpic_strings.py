#brute force
def code(s,t):
    n=len(s)
    m=len(t)
    if n!=m:
        return False
    for i in range(n):
        for j in range(i):
            if s[i]==s[j] and t[i]!=t[j]:
                return False
            if t[i]==t[j] and s[i]!=s[j]:
                return False
    return True
s = "paper"
t = "title"
print(code(s,t))
#output-True
#time complexity-o(n^2)
#space complexity-o(1)

#optimal
def code(s,t):
    n=len(s)
    m=len(t)
    dict2={}
    dict1={}
    if n!=m:
        return False
    for i in range(n):
        if s[i] in dict1:
            if dict1[s[i]]!=t[i]:
                return False
        else:
            dict1[s[i]]=t[i]
        if t[i] in dict2:
            if dict2[t[i]]!=s[i]:
                return False
        else:
            dict2[t[i]]=s[i]
    return True
s = "paper"
t = "title"
print(code(s,t))
#output-True
#time complexity-o(n)
#space complexity-o(n)