def code(s,p):
  n=len(s)
  m=len(p)
  if m>n:
    return []
  freq={}
  for ch in p:
    if ch in freq:
      freq[ch]+=1
    else:
      freq[ch]=1
  window={}
  left=0
  result=[]
  for right in range(n):
    ch=s[right]
    if ch in window:
      window[ch]+=1
    else:
      window[ch]=1
    if right-left+1>m:
      old=s[left]
      window[old]-=1
      if window[old]==0:
        del window[old]
      left+=1
    if right-left+1==m:
      if freq==window:
        result.append(left)
  return result
s="cbaebabacd"
p="abc"
print(code(s,p))
#o/p=[0, 6]
#time comp=o(n^2)
#space comp=o(1)
