def code(s):
  n=len(s)
  i=1
  while i<n:
    if n%i==0:
      repeated=""
      j=0
      while j<n:
        if s[j]!=s[j%i]:
          break
        repeated +=s[j]
        j+=1
      if j==n:
        return True
    i+=1
  return False
s="abab"
print(code(s))
#o/p=True
#time comp=o(n^2)
#space com=o(1)
