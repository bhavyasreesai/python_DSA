def code(words,pattern):
    n=len(words)
    m=len(pattern)
    result = []
    for word in words:
        dict1 ={}
        dict2={}
        valid=True
        for i in range(m):
            if pattern[i] in dict1:
                if dict1[pattern[i]]!=word[i]:
                    valid=False
                    break
            else:
                dict1[pattern[i]]=word[i]
            if word[i] in dict2:
                if dict2[word[i]]!=pattern[i]:
                    valid=False
                    break
            else:
                dict2[word[i]]=pattern[i]
        if valid:
            result.append(word)
    return result
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(code(words,pattern))
#o/p=['mee', 'aqq']
