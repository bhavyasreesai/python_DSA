def code(ransom,magazine):
    freq1={}
    freq2={}
    for ch in ransom:
        if ch in freq1:
            freq1[ch]+=1
        else:
            freq1[ch]=1
    for ch in magazine:
        if ch in freq2:
            freq2[ch]+=1
        else:
            freq2[ch]=1
    for ch in freq1:
        if ch not in freq2:
            return False
        if freq1[ch]>freq2[ch]:
            return False
    return True
ransom = "aab"
magazine = "aabr"
print(code(ransom, magazine))