def non_repeating(s):
    n=len(s)
    i=0
    freq={}
    max_length=0
    for j in range(n):
        ch=s[j]
        if ch not in freq:
            freq[ch]=0
        freq[ch]+=1
        while freq[ch]>1:
            left_char=s[i]
            freq[left_char] -= 1
            i+=1
        length=j-i+1
        if length>max_length:
            max_length=length
    return max_length
s = "abcabcbb"
print(non_repeating(s))
#output=3
#time complexity-o(n)
# space complexity-