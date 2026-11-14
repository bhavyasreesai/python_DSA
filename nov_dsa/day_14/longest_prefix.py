def code(words):

    n=len(words)
    if n==0:
        return ""
    prefix=""
    for i in range(len(words[0])):
        ch=words[0][i]
        for j in range(1,n):
            if i>len(words[j]) or words[j][i]!=ch:
                return prefix
        prefix+=ch
    return prefix

words=["flower", "flow", "flight"]
print(code(words))
#o/p=fl
#time com=o(n^2)
#space com=o(1)