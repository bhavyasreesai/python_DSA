def code(s):
  n=len(s)
  ans=0
  i=0
  while i<n:
    a=0
    e=0
    v_i=0
    o=0
    u=0
    j=i
    while j <n:
      ch=s[j]
      if ch=='a':
        a+=1
      elif ch=='e':
        e+=1
      elif ch=='i':
        v_i+=1
      elif ch=='o':
        o+=1
      elif ch=='u':
        u+=1
      else:
        break
      if a>0 and e>0 and i>0 and o>0 and u>0:
        ans+=1
      j+=1
    i+=1
  return ans
s='aeiouu'
print(code(s))

#o\p=2
#time comp=o(n^2)
#space comp=o(1)
