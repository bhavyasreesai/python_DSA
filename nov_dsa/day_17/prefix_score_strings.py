def code(words):
  freq={}
  for word in words:
    i=1
    while i<=len(word):
      prefix=word[:i]
      freq[prefix]=freq.get(prefix,0)+1
      i+=1
  result=[]
  for word in words:
    score=0
    i=1
    while i<=len(word):
      prefix=word[:i]
      score+=freq[prefix]
      i+=1
    result.append(score)
  return result
words=["abc","ab","bc","b"]
print(code(words))

#o\p=[5, 4, 3, 2]
#
