def unique(s):
  n=len(s)
  freq={}
  for ch in s:
    if ch in freq:
      freq[ch]+=1
    else:
      freq[ch]=1
  for i in range(n):
    if freq[s[i]]==1:
      return i
  return -1
s="leetcode"
print("index" , unique(s))
#output-index 0
#time complexity-o(n)
#space complexity-o(k)