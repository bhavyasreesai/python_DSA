def replacement(s,k):
    n=len(s)
    i=0
    freq={}
    max_freq=0
    max_length=0
    for j in range(n):
        ch=s[j]
        if ch not in freq:
            freq[ch]=0
        freq[ch]+=1
        if freq[ch]>max_freq:
            max_freq=freq[ch]
        while (j-i+1) - max_freq>k:
            left_char=s[i]
            freq[left_char]-=1
            i+=1
        length = j-i+1
        if length>max_length:
            max_length=length
    return max_length
s = "AABABBA"
k = 1
print(replacement(s,k))

#output=4
#time complexity-o(n)
#space complexity-o(1)