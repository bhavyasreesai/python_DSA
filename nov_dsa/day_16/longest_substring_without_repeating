def code(s):
  n=len(s)
  freq={}
  max_len=0
  left=0
  for right in range(n):
    ch=s[right]
    if ch in freq:
      freq[ch]+=1
    else:
      freq[ch]=1
    while freq[ch]>1:
      old=s[left]
      freq[old]-=1
      left+=1
    cur_len=right-left+1
    if cur_len>max_len:
      max_len=cur_len
  return max_len
s="abcabcbb"
print(code(s))
#o/p=3
#time comp=o(n)
#space comp=o(1)
