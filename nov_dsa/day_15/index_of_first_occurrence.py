def code(haystack,needle):
  n=len(haystack)
  m=len(needle)
  if m==0:
    return 0
  for i in range(n-m+1):
    j=0
    while j<m:
      if haystack[i+j]!=needle[j]:
        break
      j+=1
    if j==m:
      return i
  return -1
haystack="sadbutsad"
needle="sad"
print(code(haystack,needle))

#output-0
#time com-o(n*m)
#space com-o(1)
