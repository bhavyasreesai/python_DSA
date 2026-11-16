def code(s,k):
  n=len(s)
  freq={}
  max_len=0
  left=0
  max_freq=0
  cur_len=0
  for right in range(n):
    ch=s[right]
    if ch in freq:
      freq[ch]+=1
    else:
      freq[ch]=1
    if freq[ch]>max_freq:
      max_freq=freq[ch]
    window_len=right-left+1
    if window_len-max_freq>k:
      old=s[left]
      freq[old]-=1
      left+=1
    cur_len=right-left+1
    if cur_len>max_len:
      max_len=cur_len
  return max_len
s="AABABBA"
k=1
print(code(s,k))
#o/p=3
#time comp=o(n)
#space comp=o(1)
    
