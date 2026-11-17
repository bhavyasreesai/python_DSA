def code(s,quries):
  n=len(s)
  prefix=[0]*(n+1)
  i=0
  while i<n:
    prefix[i+1]=prefix[i]
    if s[i] in 'aeiouAEIOU' :
      prefix[i+1]+=1
    i+=1
  result=[0]*len(quries)
  i=0
  while i<len(quries):
      left=quries[i][0]
      right=quries[i][1]
      result[i]=prefix[right+1]-prefix[left]
      i+=1
  return result
s = "hello"
quries = [[0, 2], [1, 4], [0, 4]]
print(code(s,quries))
#o\p=[1, 2, 2]
