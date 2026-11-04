def common(words):
    n=len(words)
    freq1={}
    for ch in words[0]:
        if ch in freq1:
            freq1[ch]+=1
        else:
            freq1[ch]=1
    for i in range(1,n):
        freq2={}
        for ch in words[i]:
            if ch in freq2:
                freq2[ch]+=1
            else:
                freq2[ch]=1
        for ch in freq1:
            if ch in freq2:
                if freq1[ch]>freq2[ch]:
                    freq1[ch]=freq2[ch]
            else:
                freq1[ch]=0
    result=[]
    for ch in freq1:
        for i in range(freq1[ch]):
            result.append(ch)
    return result
words = ["bella", "label", "roller"]
print(common(words))
#output-['e', 'l', 'l']
#time complexity-o(n*m)
#n-no.of words, m-maxim length of a word
#space complexity-o(k+m)
#