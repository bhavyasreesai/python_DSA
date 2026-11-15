def code(s,goal):
  n=len(s)
  m=len(goal)
  if n!=m:
    return False
  combined=s+s
  for i in range(len(combined)-n+1):
    j=0
    while j<n:
      if combined[i+j]!=goal[j]:
        break
      j+=1
    if j==n:
      return True
  return False
s="abcde"
goal="cdeab"
print( code(s,goal))
#o/p=True
#time com=o(n^2)
#space comp=o(n)
