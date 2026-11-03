def groupAnagrams(strs):
    groups = {}
    for word in strs:
        freq = {}
        for ch in word:
            if ch in freq:
                freq[ch] = freq[ch] + 1
            else:
                freq[ch] = 1
        key = ""
        for ch in freq:
            key = key + ch + str(freq[ch])
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    result = []
    for key in groups:
        result.append(groups[key])
    return result
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
##output-[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
##time complexity-o(n*k^2)
##space complexity-o(n*k)
