def code(jewels,stones):
    freq1={}
    freq2={}
    for ch in stones:
        if ch in freq1:
            freq1[ch]+=1
        else:
            freq1[ch]=1
    for ch in jewels:
        if ch in freq2:
            freq2[ch]+=1
        else:
            freq2[ch]=1
    count=0
    for ch in freq2:
        if ch in freq1:
            count+=freq1[ch]
    return count
jewels = "aA"
stones = "aAAbbbb"
print(code(jewels,stones))
#output-3
#time complexity-o(n)
#space complexity-o(n)